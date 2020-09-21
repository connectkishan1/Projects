# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(__file__))
from selenium import webdriver
import unittest
import time

from sampleproject1.POM.Test.Loginpage import Loginpage
#from sampleproject1.POM.Pages.Homepage import Homepage


class LoginTest(unittest.TestCase):#inheriting TestCase from unittest
    @classmethod#for the class function always provide the annotation at classmehod
    #ther r 2 setup function 
    def setUpClass(cls):#1. this will run only once before all the test method
   #def setup(self)- 2.this will run before every test method  
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)#time to wait
     
    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        login=self.Loginpage_POM()
        login.enter_username("Admin")
        login.enter_pswd("admin123")
        login.click_login()
        
        Homepage=self.Homepage()
        Homepage.click_welcom()
        Homepage.click_logout()
        
    @classmethod
    def tearDownClass(cls):#for after all test are completed
        cls.driver.close()
        cls.driver.quit()
        print("test_completed")

#use below command for unit test using file name(pyhton Login_unittest.py in cmd prompt
#else use python -m unittest Login_unittestpy 
        
#use this cmd in spider as well to display unittest        
if __name__=="__main__":
    unittest.main()
    
        
# -*- coding: utf-8 -*-


