import inspect

import yaml
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self,name):
        self._params["name"]=name
        # 改造为yaml数据驱动的操作步骤
        self.steps("../page/search.yaml")


        #send alibaba
        # self.find(MobileBy.ID,"search_input_text").send_keys(name)
        # self.find(MobileBy.XPATH,"//*[@text='BABA']").click()
        # self.find(MobileBy.XPATH,f"//*[contains(@resource-id,'stock_item_container')]//*[@text='{name}']/../..//*[@text='加自选']").click()#查询加自选


        # with open("../page/search1.yaml", encoding="utf-8") as f:
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
        #                 elemet.send_keys(value)
    def add(self,name):
        self._params["name"] = name
        self.steps("../page/search.yaml")

    def is_choose(self, name):
        self._params["name"] = name
        return self.steps("../page/search.yaml")
    def reset(self,name):
        self._params["name"] = name
        return self.steps("../page/search.yaml")

