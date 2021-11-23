import os
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
            #外部取值设定udid可以运行多个设备
            caps["udid"]=os.getenv("udid",None)
            caps['noReset'] = "true"

            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
         #    设置与selenium gird的链接
            self._driver = webdriver.Remote("http://192.168.249.51:4444/wd/hub", caps)
         else:
               self._driver.start_activity(self._package,self._activity)
         self._driver.implicitly_wait(3)
         return self
      def main(self) -> Main:
            self._driver.save_screenshot('main.png')
            return Main(self._driver)
