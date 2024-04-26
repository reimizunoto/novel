from src.novel import Novel
from utils.setting import Xs33Setting
from urllib.parse import quote
from lxml import etree
from html2text import html2text
import re
import unicodedata as ucd

class Xs33(Novel):
    def __init__(self, title: str):
        self.title = title
        self.link = 'https://www.x33xs6.com'
        self.setting = Xs33Setting()
        self.setting.set_headers({'Referer': 'https://www.x33xs6.com/'})
        
    def _search(self):
        search_url = f'https://www.x33xs6.com/search.php?keyword={quote(self.title,'utf-8')}'
        res = self._html(search_url)
        html = etree.HTML(res.text)
        # get the search results
        articles = html.xpath('//div[@class="result-list gameblock-result-list"]/div/div[2]/h3/a/text()')
        info_list = html.xpath('//div[@class="result-list gameblock-result-list"]/div/div[2]/p/text()')
        url_list = html.xpath('//div[@class="result-list gameblock-result-list"]/div/div[2]/h3/a/@href')
        print('<----------------search results-------------------->')
        for i, article in enumerate(articles):
            print(f'{i} : {article.strip()}====>{info_list[i]}')
        index = input('please input the index of the novel you want to download: ')
        index = int(index)
        # get the chapters info
        url = self.link + url_list[index]
        html = self._html(url).text
        chapters = re.findall(r'html">(.*?)</a></dd>', html)
        chapter_urls = re.findall(r'<dd><a href="(.*?)">', html)
        chapter_info = {k:v for k,v in zip(chapters, chapter_urls)}
        self.chapter_info = chapter_info
        # for chapter, url in chapter_info.items():
        #     print(f'{chapter} : {url}')
    
    def _download_chapter(self):
        for chapter, url in self.chapter_info.items():
            chapter_url = self.link + url
            print(chapter_url)
            html = self._html(chapter_url).text
            html = etree.HTML(html)
            content = html.xpath('//div[@id="content"]/text()')
            # print(content)
            con = ''
            for item in content:
                con += ucd.normalize('NFKC', item.strip()) + '\n'
            self._save_chapter({'title': chapter, 'content': con})
            break
            
    def download(self):
        self._search()
        self._download_chapter()