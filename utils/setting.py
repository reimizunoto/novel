
# import requests
import settings

class setting:
    def __init__(self):
        self.headers = {}
        self.cookies = {}

    def set_headers(self, headers):
        self.headers = headers

    def set_cookies(self, cookies):
        self.cookies = cookies
    
    def get_headers(self):
        return self.headers

    def get_cookies(self):
        return self.cookies

class QidianSetting(setting):
    def __init__(self):
        self.headers = settings.QIDIAN_HEADERS
        self.cookies = settings.QIDIAN_COOKIES

class DushugeSetting(setting):
    def __init__(self):
        self.headers = settings.DUSHUGE_HEADERS
        self.cookies = settings.DUSHUGE_COOKIES