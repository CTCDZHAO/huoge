from selenium import webdriver
import time
from selenium.webdriver import ActionChains
class TestActionChians:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_click(self):
        element_click=self.driver.find_element_by_xpath('//input[@value="click me"]')
        element_doubleclick=self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        action=ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        time.sleep(3)
        action.perform()
    def test_moveelement(self):


