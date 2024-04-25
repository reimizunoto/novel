import requests
from utils.setting import DushugeSetting
from src.novel import Novel

class Dushuge(Novel):
    def __init__(self, title):
        self.link = 'https://www.dushuge6.com/search.php?keyword='
        self.title = title
        
    def get_novel_info(self):
        s = DushugeSetting()
        respone = requests.get(self.link + self.title, headers=s.get_headers(), cookies=s.get_cookies())
        if respone.status_code != 200:
            print('获取小说信息失败')
            return None
        print(respone.text)

if __name__ == "__main__":
    dushuge = Dushuge()
    dushuge.get_novel_info()