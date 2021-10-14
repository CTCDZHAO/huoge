"""
page类：继承basepage使用basepage中的构造方法
       Python的性质会主动先寻找继承的类

"""

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_winwork_main_test.page.add_member import AddMember
from selenium_winwork_main_test.page.base_page import BasePage



class Main(BasePage):
    # 对basepage中的_base_url重新赋值，继承的关系可以直接使用父级的类和变量
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_addmember(self):
        # 跳转至成员列表页（通讯录）
        self.find(By.ID,'menu_contacts').click()
        # WebDriverWait(self._driver,10).until(
        #     EC.element_to_be_clickable((By.XPATH,'//main[@id="main"]//div[@class="ww_operationBar"]/a[1]'))
        # )
        self.wait_for_click((By.XPATH, '//main[@id="main"]//div[@class="ww_operationBar"]/a[1]'))#显示等待
        self.find(By.XPATH, '//main[@id="main"]//div[@class="ww_operationBar"]/a[1]').click()
        return AddMember(self._driver)
