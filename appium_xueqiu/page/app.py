from time import sleep

import yaml
from appium import webdriver

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.main import Main


class App(BasePage):
      _package="com.xueqiu.android"
      _activity=".view.WelcomeActivityAlias"

      def start(self):
         if self._driver == None:
            caps={}
            caps["platformName"] = "Android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps['noReset'] = "true"
            # caps['udid']=yaml.safe_load(open("../page/conifiguration.yaml"))['caps']['udid']
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True

            # self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
         #    设置与selenium gird的链接
            self._driver = webdriver.Remote("http://192.168.249.51:4444/wd/hub", caps)
         else:
               self._driver.start_activity(self._package,self._activity)
         self._driver.implicitly_wait(3)
         return self
      def main(self) -> Main:
            self._driver.save_screenshot('main.png')
            return Main(self._driver)
