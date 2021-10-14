from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium_wekwork_mian.page.add_member import AddMember


class Main:
    def __init__(self):
        options=Options()
        options.debugger_address="127.0.0.1:9223"
        self.driver=webdriver.Chrome(options=options)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    def goto_add_memeber(self):
        # click add member
        self.driver.find_element(By.XPATH,'//a[@node-type="addmember"]').click()
        return AddMember(self.driver)