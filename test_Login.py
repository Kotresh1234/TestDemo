from selenium import webdriver
import pytest
from selenium.webdriver.common.action_chains import ActionChains
  
# import KEYS
from selenium.webdriver.common.keys import Keys
import time
class Test_Login():
    
    def test_Login_001(self):
        self.driver = webdriver.Chrome("D:\\Learning\\chromedriver.exe")
        time.sleep(2)
        self.driver.get("https://www.google.com/?gws_rd=ssl")
        time.sleep(2)
        self.driver.find_element_by_name("q").send_keys("jai mata di")
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul/li[4]/div/div[2]/div[1]/span/b").click()
#         action = ActionChains(self.driver)
#
# # perform the oepration
#         action.click("ENTER").perform()
        self.driver.find_element_by_name("btnK").click()
        time.sleep(2)
        # yield driver
        # self.driver.quit()
