from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.search import Search


class Market(BasePage):
    def go_to_search(self):
        #click
        self.find(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self._driver)