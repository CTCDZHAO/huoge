from selenium import webdriver

class Base:
    def setup(self):
        self.driver =webdriver.Chrome()

        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
# from selenium import webdriver
# import os
# class Base:
#     def setup(self):
#         browser=os.getenv("browser")
#         if browser=='firefox':
#             self.driver=webdriver.Firefox()
#         elif browser=='headless':
#             self.driver=webdriver.PhantomJS()
#         else
#             self.driver=webdriver.Chrome()
#         self.driver.implicitly_wait(3)
#         self.driver.maximize_window()
#     def teardown(self):
#         self.driver.quit()