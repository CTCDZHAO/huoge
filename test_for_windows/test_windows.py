#切换windows
#重点是句柄
#切换至frame
from time import sleep

from test_for_windows.base import Base
class TestWindows(Base):
    def test_window(self):
       self.driver.implicitly_wait(4)
       self.driver.get('https://www.baidu.com')
       self.driver.find_element_by_link_text("登录").click()
       print(self.driver.current_window_handle)
       print(self.driver.window_handles)
       self.driver.find_element_by_link_text("立即注册").click()
       print(self.driver.current_window_handle)
       print(self.driver.window_handles)
       windows=self.driver.window_handles
       self.driver.switch_to_window(windows[-1])

       self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
       sleep(3)