import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver:WebDriver
    _black_list=[(By.ID,"iv_action_back")]#定义一个黑名单列表
    def __init__(self,driver:WebDriver=None):
        self._driver=driver

    def find(self,locator,value):
        try:
          element=self._driver.find_element(locator,value)
          return  element
        except:
            for black in self._black_list:#遍历黑名单
                elements = self._driver.find_elements(*black)#获取黑名单元素
                if len(elements) >0:#判断是否获取
                    elements[0].click()#存在则进行点击
            return self.find(locator,value)#处理完黑名单，后重新进行元素查找

    # def click(self,locator,value):
    #     return self.find(locator,value).click()
    def steps(self,path):
        with open(path) as f:
            steps=yaml.safe_load(f)
            print(steps)
        element=None
        for step in steps:
            if "by" in step.keys():
                element=self.find(step["by"],step["locator"])
            if "action" in step.keys():
                action=step["action"]
                if action =="click":
                    element.click()
# if __name__ == '__main__':
#  BasePage().steps("../page/main.yaml")