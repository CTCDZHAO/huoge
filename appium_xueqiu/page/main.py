from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage


class Main(BasePage):
    def go_to_search(self):
        # sleep()
        self.find(By.ID,"tv_search").click()
        # self.steps("../page/main.yaml")
    def go_to_windows(self):
        self.find(By.ID,"post_status").click()
        self.find(By.ID, "tv_search").click()
