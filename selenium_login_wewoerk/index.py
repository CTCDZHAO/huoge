from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_login_wewoerk.login import Login
from selenium_login_wewoerk.register import Register


class Index:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')
    def go_to_login(self):
        # click_login
        # $('.index_top_operation_loginBtn')登录按钮
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return Login(self.driver)
    def go_to_register(self):
        # $('.index_head_info_pCDownloadBtn')
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)