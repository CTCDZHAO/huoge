from time import sleep

from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Register:
    def __init__(self,driver:WebDriver):
        self._driver=driver
    def register_ture(self):
        #send_keys,click,
        # corp_name
        self._driver.find_element(By.ID,'corp_name').send_keys('hello11')
        self._driver.find_element(By.ID,'manager_name').send_keys('moren')
        sleep(5)
        self._driver.quit()
        return True
    def register_false(self):
        #send_keys,click,
        # corp_name
        self._driver.find_element(By.ID,'corp_name').send_keys('hello11')
        self._driver.find_element(By.ID,'manager_name').send_keys('')
        sleep(5)
        self._driver.quit()
        return False