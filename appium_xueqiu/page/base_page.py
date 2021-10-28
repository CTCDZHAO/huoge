import logging
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from appium_xueqiu.page.wrapper import handle_black



class BasePage:
    # logging.basicConfig(level=logging.INFO)
    _driver:WebDriver
    # _black_list=[(By.ID,"iv_action_back")]#定义一个黑名单列表
    # _max_num = 3
    # _error_num = 0
    def __init__(self,driver:WebDriver=None):
        self._driver=driver
    @handle_black
    def find(self,locator,value: str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    def finds(self,locator,value:str = None):
        elements:list
        if isinstance(locator,tuple):
            elements=self._driver.find_elements(*locator)
        else:
            elements=self._driver.find_element(locator,value)
        return elements
    @handle_black
    def find_and_get_text(self,locator,value:str=None):
        element:WebElement
        if isinstance(locator,tuple):
            element_text=self._driver.find_element(*locator).text
        else:
            element_text=self._driver.find_element(locator,value).text
        return element_text

    def steps(self,path,name):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)[name]
            for step in steps:
                elemet = None
                if "action" in step.keys():
                    action = step["action"]
                    if "click" == action:
                       self.find(step["by"], step["locator"]).click()
                    if "send" == action:
                        self.find(step["by"], step["locator"]).send_keys(step["value'"])
                    if "len > 0" == action:
                        eles = self.finds(step["by"], step["locator"])
                        return len(eles) > 0

