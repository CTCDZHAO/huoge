from time import sleep

from selenium.webdriver.android.webdriver import WebDriver

from selenium_login_wewoerk.index import Index


class TestRegister:
    # def __init__(self,driver:WebDriver):
        # self._driver=driver
    def setup(self):
        self.index=Index()
    def test_register(self):
        # self.index.go_to_login().go_to_register().register()
        self.index.go_to_register().register()
        # sleep(5)

        # self._driver.quit()
        #