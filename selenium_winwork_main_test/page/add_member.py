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
    def get_member(self):
        elements=self.finds_element(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')

        return [element.get_attribute("title") for element in elements]