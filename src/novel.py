from utils.setting import setting
import os
import requests

class Novel:
    def __init__(self):
        self.title = None
        self.author = None
        self.link = None
        self.intro = None
        self.chapters = []
        self.setting = setting()
    
    def _save_chapter(self, chapter: dict):
        novel_path = f'novel/{self.title}/'
        os.makedirs(novel_path, exist_ok=True)
        chapter_title = f'{chapter["title"]}.txt'
        
        print(f'Saving {chapter_title}...')
        with open(novel_path + chapter_title, 'w', encoding='utf-8') as f:
            f.write(chapter['content'])
            print(f'{chapter_title} saved.')
    
    def _html(self, url: str, params: dict={}, mode='get'):
        match mode:
            case 'get':
                response = requests.get(url, headers=self.setting.headers, cookies=self.setting.cookies, params=params)
            case 'post':
                response = requests.post(url, headers=self.setting.headers, cookies=self.setting.cookies, data=params)
        
        if response.status_code != 200:
            print(f'Error: {response.status_code} {response.reason}')
            return None
        return response