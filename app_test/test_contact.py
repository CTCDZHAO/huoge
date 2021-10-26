# 企业微信
"""

"""
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestQiWinXin:
    def setup_class(self):
        caps = {}
        caps["deviceName"] = "emulator-5554"
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps['noReset']="Ture"#无需二次登陆
        caps['skipServerInstalltion']=True# 跳过UI2的安装
        caps['skipDeviceInitialization']=True# 新的Appium版本支持通过desired capbilities选项来跳过初始化操作,跳过安装appium settings
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
    def setup(self):
        pass
    def teardown(self):
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()
    def teardown_class(self):
        self.driver.quit()

    def test_contact(self):
        print('添加成员')
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()

        #输入信息
        nameelement=self.driver.find_element(MobileBy.XPATH,"//*[@text='姓名　']/../*[@class='android.widget.EditText']")
        nameelement.send_keys("霍格name1")
        memeberelement=self.driver.find_element(MobileBy.XPATH,"//*[@text='帐号　']/..//*[@class='android.widget.EditText']")
        memeberelement.send_keys('账号信息')
        genderelement=self.driver.find_element(MobileBy.XPATH,"//*[@text='性别']/../*[@class='android.widget.RelativeLayout']")
        genderelement.click()
        melaelement=self.driver.find_element(MobileBy.XPATH,"//*[@text='女']")
        melaelement.click()
        phonememberelement=self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/gc6")
        phonememberelement.send_keys('13723424884')
        saveelement=self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/alo")
        saveelement.click()
        toastelement=self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']")
        print(toastelement.text)






