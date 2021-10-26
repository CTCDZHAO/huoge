# 脚本录制雪球查询阿里巴巴
"""
改造1：pytest模式
改造2：改造成可维护的代码形式，绝对不允许绝对路径的存在
改造3：将自动生成的find_elemrnt_by_*改造为find_element(MobileBy.**)
改造4：添加断言
"""
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueQiu:
    def setup_class(self):
        caps = {}
        caps["deviceName"] = "emulator-5554"
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
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
    @pytest.mark.parametrize('searchkey,serchresult',[
        ('alibaba','阿里巴巴'),
        ('jd','京东')
    ])
    def test_search(self,searchkey,serchresult):
        el6 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el6.click()
        el7 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el7.send_keys(searchkey)
        el8 = self.driver.find_element_by_xpath('//*[@text="阿里巴巴"]')
        el8.click()
        el4 = self.driver.find_elements(MobileBy.XPATH,
                                        f"//*[@text='{serchresult}']/../..//*[@text='加自选']")
        if len(el4)>0:
            el4[0].click()
            self.driver.find_element(MobileBy.XPATH,f"//*[@text='{serchresult}']/../..//*[@text='已添加']")
        else:
            print("已加自选")


