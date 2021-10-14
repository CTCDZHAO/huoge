"""
basepage对类的初始化：
       如果传值则赋值
       如果不传值则直接使用默认值初始化
       basepage的初步的封装
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    _driver=None
    _base_url=""
    def __init__(self,driver:WebDriver=None):
        if driver is None:
            options=Options()
            options.debugger_address='127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(3)
        else:
            self._driver=driver
        if self._base_url !="":
            self._driver.get(self._base_url)
    def find(self,by,locator):#by定位方式，locator定位地址
         return self._driver.find_element(by,locator)
    def finds_element(self,by,locator):
        return self._driver.find_elements(by,locator)
    def wait_for_click(self,locator,time=10):
        #显示等待元素是否存在
        WebDriverWait(self._driver, time, 0.5).until(
            EC.element_to_be_clickable(locator)
        )
    def wait_for_element(self,conditions,time=10):
        WebDriverWait(self._driver, time, 0.5).until(
            conditions
        )
