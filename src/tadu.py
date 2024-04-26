import re
import requests
from lxml import etree
# from urllib.parse import quote
from html2text import html2text
from utils.setting import BigeeSetting
from src.novel import Novel

class Tadu(Novel):
    def __init__(self, title):
        self.title = title
        self.link = 'https://www.tadu.com'
        self.setting = BigeeSetting()
        self.setting.set_headers({'Referer': 'https://www.tadu.com/search'})
    
    def _search(self):
        params = {
            'query': self.title
        }
        url = 'https://www.tadu.com/search'
        res = self._html(url, params=params, mode='post')
        html = etree.HTML(res.text)
        articles = html.xpath('//a[@class="bookNm"]/span/text() | //a[@class="bookNm"]/text()')
        info_list = html.xpath('//a[@class="bookIntro"]/text()')
        url_list = html.xpath('//a[@class="bookNm"]/@href')
        print('<-------------query result-------------->')
        for i, article in enumerate(articles):
            print(f'{i} : {article} --- {info_list[i]}')
        index = input('Please select the index of the novel you want to download: ')
        if index.isdigit():
            index = int(index)
        if index < 0 or index >= len(articles):
            print('Error: index out of range')
            return None
        res = self._html(self.link + url_list[index])
        # print(res)
        html = etree.HTML(res.text)
        chapters = html.xpath('//div[@class="lf lfT hidden"]/li/div/a/text()')
        urls = html.xpath('//div[@class="lf lfT hidden"]/li/div/a/@href')
        chapters_info = {key : self.link + value for key, value in zip(chapters, urls)}
        self.chapters_info = chapters_info
        # print(f'Novel: {chapters_info}')

    def _download_chapter(self):
        for chapter, url in self.chapters_info.items():
            html = self._html(url).text
            
            url = re.findall(r'<input type="hidden" id="bookPartResourceUrl" value="(.*?)">', html)[0]
            url = self.link + url
            res = self._html(url).json()
            content = res['data']['content']
            content = html2text(content)
            self._save_chapter({'title': chapter.replace(':', '-'), 'content': content})
            break
    
    def download(self):
        self._search()
        self._download_chapter()
        