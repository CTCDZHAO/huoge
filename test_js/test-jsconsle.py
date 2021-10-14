from selenium import webdriver
from test_js.base import Base

class TestJS(Base):
    def test_js_console(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id("kw").send_keys('selenium测试')
        self.driver.execute_script('')