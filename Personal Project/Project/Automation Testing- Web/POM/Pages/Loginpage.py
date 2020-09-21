# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

class LoginPage():#any name
    def __init__(self,driver):
        self.driver=driver
        self.username_textbox_id="txtUsername"
        self.password_textbox_id="txtPassword"
        self.login_bottn_name="Submit"
    
    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
    
    def enter_userpswd(self,userpswd):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(userpswd)
    def click_login(self):
        self.driver.find_element_by_name(self.login_bottn_name).click()
        


