from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# # class TestWait:
# #     def setup(self):
# #         self.driver=webdriver.Chrome()
# #         self.driver.get('https://ceshiren.com/')
# #         self.driver.implicitly_wait(3)
# #     def test_wait(self):
# #         self.driver.find_element_by_xpath('//li[@title="所有分类"]').click()
# #
# #         # def wait(x):
# #         #     return len(self.driver.find_element())
# #         WebDriverWait(self.driver,20,0.5).until(
# #             EC.presence_of_element_located((By.XPATH,'title="过去一年、一个月、一周或一天中最活跃的话题"'))
# #         )
# #         self.driver.find_element_by_xpath('title="过去一年、一个月、一周或一天中最活跃的话题"').click()

class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(3)
    def test_wait(self):
        self.driver.find_element(By.CSS_SELECTOR,'[id=kw]').send_keys('霍格沃兹测试学院')
        self.driver.find_element(By.XPATH,'')
