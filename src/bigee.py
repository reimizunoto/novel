import requests
import re
from urllib.parse import quote
from html2text import html2text
from utils.setting import BigeeSetting
from src.novel import Novel

class Bigee(Novel):
    def __init__(self, title):
        self.title = quote(title, 'utf-8')
        self.link = f'https://www.bigee.cc/user/search.html?q={self.title}'
        self.setting = BigeeSetting()
        self.setting.set_headers({'Referer': f'https://www.bigee.cc/s?q={self.title}'})
        
    def _set_info(self, info_dict: dict):
        base_url = 'https://www.bigee.cc'
        
        self.title = info_dict['articlename']
        self.author = info_dict['author']
        self.link = base_url + info_dict['url_list']
        self.intro = info_dict['intro']
    
    def _search(self):
        # s.set_headers({'Referer': f'https://www.bigee.cc/s?q={self.title}'})
        res = requests.get(self.link, headers=self.setting.get_headers(), cookies=self.setting.get_cookies())
        if res.status_code != 200:
            print('Error: Failed to get search result')
            return None
        info_list = res.json()
        # print(self.setting.get_headers())
        # print(info_list)
        print('<----------------query result---------------->')
        for i, info in enumerate(info_list):
            print(f'{i} : {info['articlename']}')
        index = int(input('Please select the novel you want to download: '))
        # set book info
        self._set_info(info_list[index])
    
    def _get_chapters(self):
        # get chapters
        res = requests.get(self.link, headers=self.setting.get_headers(), cookies=self.setting.get_cookies())
        if res.status_code != 200:
            print('Error: Failed to get chapters')
            return None
        html = res.text
        # get chapters and urls
        chapters = re.findall(r'html">(.*?)</a></dd>', html)
        urls = re.findall(r'<dd><a href ="(.*?)">', html)
        # print(chapters)
        # print(urls)
        base_url = 'https://www.bigee.cc'
        chapter_info = {}
        for key, value in zip(chapters, urls):
            # 排除干扰信息
            if not key.startswith('第'):
                continue
            chapter_info[key.replace(' ', '-')] = base_url + value
        # print(chapter_info)
        # save chapters info
        self.chapter_info = chapter_info
    
    def _download_chapters(self):
        # get chapter content
        for chapter, url in self.chapter_info.items():
            res = requests.get(url, headers=self.setting.get_headers(), cookies=self.setting.get_cookies())
            if res.status_code != 200:
                print('Error: Failed to get chapter content')
                return None
            html = res.text
            content = re.findall(r'<div id="chaptercontent" class="Readarea ReadAjax_content">(.*?)请收藏本站', html)[0].strip()
            content = html2text(content)
            # print(content)
            # download and save chapter
            self._save_chapter({'title': chapter, 'content': content})
            break
    
    def download(self):
        self._search()
        self._get_chapters()
        self._download_chapters()