from selenium import webdriver
from test_js.base import Base

class TestFile(Base):
    def test_file(self):
        self.driver.get('https://www.baidu.com')

