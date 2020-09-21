# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import os
import sys
import time
import HtmlTestRunner


class LoginTest(unittest.TestCase):#inheriting TestCase from unittest
    @classmethod#for the class function always provide the annotation at classmehod
    #ther r 2 setup function 
    def setUpClass(cls):#1. this will run only once before all the test method
   #def setup(self)- 2.this will run before every test method  
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)#time to wait
     
    def test_01_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        time.sleep(2)
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)
        
    def test_02_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("kk")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        time.sleep(2)
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):#for after all test are completed
        cls.driver.close()
        cls.driver.quit()
        print("test_completed")

#use below command for unit test using file name(pyhton Login_unittest.py in cmd prompt
#else use python -m unittest Login_unittestpy 
        
#use this cmd in spider as well to display unittest        
if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\Radhakrishna\sampleproject1"))
    
        

