import time
from selenium import webdriver

class TestHoukgewozi:
    def setup(self):
        # self.driver=webdriver.Chrome(executable_path='driver path')#手动添加driver路径
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
    def test_huogewozi(self):

        self.driver.get('https://testerhome.com/')
        self.driver.find_element_by_link_text('社团').click()
        self.driver.find_element_by_link_text("霍格沃兹学院").click()
        self.driver.find_elements_by_xpath('')