
import time
from selenium import webdriver
from unittest.suite import TestSuite
import unittest
import HtmlTestRunner

class TestCase(unittest.TestCase):

 def setUp(self):
     unittest.TestCase.setUp(self)

 def tearDown(self):
     unittest.TestCase.tearDown(self)

 def test_Demo_Windows(self):
     # value = input("Please Enter The Value :\n ")
     # print(f'Your Entered Value {value}')
     a=1
     b=2
     c=a+b
     print(f'Your Entered Value {c}')
     assert c==3
     True
     print("Assertion Pass")
     
 def test_Login_001(self):
    self.driver = webdriver.Chrome("D:\\Learning\\chromedriver.exe")
    time.sleep(2)
    self.driver.get("https://www.google.com/?gws_rd=ssl")
    time.sleep(2)
    self.driver.find_element_by_name("q").send_keys("jai mata di")
    time.sleep(2)
    self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul/li[4]/div/div[2]/div[1]/span/b").click()
#            action.click("ENTER").perform()
    self.driver.find_element_by_name("btnK").click()
    time.sleep(2)
        # yield driver
        # self.driver.quit()

     
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Learning/AutomationQA/Report/'))