from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium_winwork_main_test.page.add_member import AddMember


class Contacts:
    def __init__(self,driver:WebDriver):
        self._driver=driver
    def add_member(self):
        self._driver.find_element(By.XPATH,'//main[@id="main"]//div[@class="ww_operationBar"]/a[1]').click()

        return AddMember(self._driver)