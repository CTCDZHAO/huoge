#设置一个
import logging

import allure
from selenium.webdriver.common.by import By

def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args,**kwargs):
        from appium_xueqiu.page.base_page import BasePage
        _black_list = [
            (By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),
        ]
        _max_num = 3
        _error_num = 0
        instance: BasePage = args[0]
        # instance= args[0]
        try:
           logging.info("run"+func.__name__+"\n args: \n"+repr(args[1:])+"\n kwargs: \n"+repr(kwargs))
           element=func(*args, **kwargs)
           _error_num = 0
           instance._driver.implicitly_wait(10)
           return element
        except Exception as e:
            instance.screenshot("tmp.png")
            with open("tmp.png","rb") as f:
                content=f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            logging.error("element not found,try find")
            instance._driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            # 处理黑名单里面的弹框
            for ele in _black_list:
                elelist = instance._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再去查找目标元素
                    return instance.find(*args, **kwargs)
            raise e
    return wrapper