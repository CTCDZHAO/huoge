from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class Main(BasePage):
    def go_to_search(self):
        # sleep()
        self.steps("../page/main.yaml")
