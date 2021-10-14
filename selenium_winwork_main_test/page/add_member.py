from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium_winwork_main_test.page.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        # send_keys
        self.find(By.ID, 'username').send_keys('username')
        self.find(By.ID, 'memberAdd_acctid').send_keys('engishname')
        self.find(By.ID, 'qui_inputText ww_inputText ww_telInput_mainNumber').send_keys('11111111')
        self.find(By.XPATH,
                                  '//*[@id="js_contacts45"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        sleep(5)
        self._driver.quit()

        return True
    def update_page(self):
        # 获取页面信息的方法
        content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        return [int(x) for x in content.split('/', 1)]

    def get_member(self,value):
        self.wait_for_click(By.XPATH,'//th[@class="member_colRight_memberTable_th_Checkbox"]')#判断元素是否加载完成
        content:str=self.find(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
        cur_page,total_page=self.update_page()
        # list=[]
        # while True:
        #     elements=self.finds_element(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        #     for element in elements:
        #         list.append(element.get_attribute("title"))
        #     content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        #     cur_page, total_page = [int(x) for x in content.split('/', 1)][0]
        #     if cur_page ==total_page:
        #         return list
        #     self.find(By.CSS_SELECTOR, 'js_next_page').click()
        """更新增加人员判断增加效率"""

        while True:
            elements = self.finds_element(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for element in elements:
                if value==element.get_attribute("title"):
                    return True
            cur_page=self.update_page()[0]
            if cur_page == total_page:
                return False
            self.find(By.CSS_SELECTOR, 'js_next_page').click()

