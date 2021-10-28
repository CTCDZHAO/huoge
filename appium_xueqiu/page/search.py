import yaml
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self,name):
        # 改造为yaml数据驱动的操作步骤
        self.steps("../page/search1.yaml")


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
        self.steps("../page/search4.yaml")
    def is_choose(self,name):
        # 改造为yaml数据驱动的操作步骤
        return self.steps("../page/search1.yaml")

        # eles=self.finds(MobileBy.XPATH,f"//*[contains(@resource-id,'stock_item_container')]//*[@text='{name}']/../..//*[@text='已添加']")#搜已添加
        # return len(eles) > 0#如果大于0则已添加存在


        # with open("../page/search2.yaml", encoding="utf-8") as f:
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
        #             if "len > 0" == action:
        #                  eles=self.finds(step["by"],step["locator"])
        #                  return len(eles) >0
    def reset(self,name):
        return self.steps("../page/search3.yaml")

