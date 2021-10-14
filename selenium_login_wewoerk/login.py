from selenium.webdriver.android import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By

# from selenium_login_wewoerk.index import Index
from selenium_login_wewoerk.register import Register


class Login:
    def __init__(self,driver:WebDriver):
        self._driver=driver

    def scanf(self):
        pass
    def go_to_register(self):
         self._driver.implicitly_wait(3)
         self._driver.find_element(By.XPATH,'//a[@class="login_registerBar_link"]').click()
         return Register(self._driver)