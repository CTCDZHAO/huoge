from appium import webdriver

from app_test.page.base_page import BasePage
from app_test.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver==None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps['noReset'] = "true"
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()
        return self
    def restart(self):
        pass
    def stop(self):
        pass
    def stop(self):
        pass
    def main(self) -> Main:
        return Main(self._driver)