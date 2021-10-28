import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.market import Market


class Main(BasePage):
    def go_to_market(self,):
        #改造为yaml数据驱动的操作步骤
        self.steps("../page/main.yaml")
        #click
        # self.find(MobileBy.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']").click()

        # with open("../page/main.yaml", encoding="utf-8") as f:
        #     steps = yaml.safe_load(f)
        #     for step in steps:
        #         elemet=None
        #         if "by" in step.keys():
        #             elemet=self.find(step["by"],step["locator"])
        #         if "action" in step.keys():
        #             action = step["action"]
        #             if "click" == action:
        #                 elemet.click()
        #             if "send" == action:
        #                 value = step["value"]
        #                 print(f"send{value}")
        # print(step)
        return Market(self._driver)
if __name__ == '__main__':
    Main().go_to_market()
