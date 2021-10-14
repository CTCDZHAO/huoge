from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class AddMember:
    def __init__(self,driver:WebDriver):
        self._driver=driver
    def add_member(self):
        # send_keys
        self._driver.find_element(By.ID,'username').send_keys('username')
        self._driver.find_element(By.ID,'memberAdd_acctid').send_keys('engishname')
        self._driver.find_element(By.ID,'qui_inputText ww_inputText ww_telInput_mainNumber').send_keys('11111111')
        self._driver.find_element(By.XPATH,'//*[@id="js_contacts45"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        sleep(5)
        self._driver.quit()

        return True
    def get_member(self):
        # self._driver.find_elements(By.XPATH,'//tbody[@id="member_list"]//td[@class="member_colRight_memberTable_td"][1]')
        elements=self._driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        # list = [element.get_attribute("title") for element in elements]
        # for element in elements:
        #     list.append(element.get_attribute("title"))
        # return list
        return [element.get_attribute("title") for element in elements]