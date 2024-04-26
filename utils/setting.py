
# import requests
import settings

class setting:
    def __init__(self):
        self.headers = {}
        self.cookies = {}

    def set_headers(self, headers: dict):
        for key, value in headers.items():
            self.headers[key] = value

    def set_cookies(self, cookies: dict):
        for key, value in cookies.items():
            self.cookies[key] = value
    
    def get_headers(self: dict):
        return self.headers

    def get_cookies(self: dict):
        return self.cookies

class QidianSetting(setting):
    def __init__(self):
        self.headers = settings.QIDIAN_HEADERS
        self.cookies = settings.QIDIAN_COOKIES

class DushugeSetting(setting):
    def __init__(self):
        self.headers = settings.DUSHUGE_HEADERS
        self.cookies = settings.DUSHUGE_COOKIES

class BigeeSetting(setting):
    def __init__(self):
        self.headers = settings.BIGEE_HEADERS
        self.cookies = settings.BIGEE_COOKIES
        
class TaduSetting(setting):
    def __init__(self):
        self.headers = settings.TADU_HEADERS
        self.cookies = settings.TADU_COOKIES
        
class Xs33Setting(setting):
    def __init__(self):
        self.headers = settings.XS33_HEADERS
        self.cookies = settings.XS33_COOKIES