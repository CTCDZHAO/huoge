"""remote复用之后使用cookie登录企业微信"""
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestCaseone:
    def setup(self):
        option=Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=option)
        # self.driver=webdriver.Chrome()


    def teardown(self):
        self.driver.quit()
    def test_demo(self):
        # self.driver.get('')
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        print(self.driver.get_cookies())
        db=shelve.open("cookies")#shelve本地保存数据，可以当做小型数据库
        db["cookies"]=self.driver.get_cookies()
        cookies=db["cookies"]
        for cookie in cookies:
            if "expiry" in cookie:
               cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element(By.ID,'menu_contacts')