from selenium import webdriver
import json


class CookieLogin:

    def __init__(self):
        pass

    def cookie_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://test.hrhbbx.com/')
        self.driver.maximize_window()
        f1 = open('cookie.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)

        for i in cookie:
            # print(i)
            # print('=' * 10)
            self.driver.add_cookie(i)

        self.driver.refresh()

    def quite(self):
        self.driver.quit()
