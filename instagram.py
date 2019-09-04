# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from re import findall
from time import sleep
from fake import *
import boto3
import logging
from botocore.exceptions import ClientError
from guicontrol import *
from fivesim import *

class inst(unittest.TestCase):
    def inst_setup(self):
        self.person = jload()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def inst_start(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        driver.find_element_by_name("emailOrPhone").click()
        driver.find_element_by_name("emailOrPhone").clear()
        tel = buy_number('instagram')
        tel_number = tel[1]
        tel_code = tel[0]
        driver.find_element_by_name("emailOrPhone").send_keys(tel_number)
        driver.find_element_by_xpath("//span[@id='react-root']/section/main/article").click()
        driver.find_element_by_name("fullName").click()
        driver.find_element_by_name("fullName").clear()
        driver.find_element_by_name("fullName").send_keys(self.person["first_last"])
        driver.find_element_by_xpath("//span[@id='react-root']/section/main/article").click()
        driver.find_element_by_xpath("//span[@id='react-root']/section/main/article").click()
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(self.person['login'])
        sleep(5)
        press('tab')
        sleep(1)
        press('enter')
        sleep(1)
        press('enter')
        sleep(1)
        press('tab')
        sleep(3)
        tp2(self.person['password'])
        press('tab')
        press('enter')
        press('tab')
        press('enter')
        write_instagram_json(tel_number)
        sleep(5)
        set_ok(tel_code)
        code1 = order_status(tel_code)
        tp2(code1)
        press('enter')
        sleep(5)
        press('enter')
        sleep(5)
        set_double(tel_code)
        set_ok(tel_code)
        code2 = order_status(tel_code)
        while code1 == code2:
            code2 = order_status(tel_code)
            print(code2)
        tp2(code2)
        press('enter')
        sleep(10) 
        write_instagram_json(tel_number)
        time.sleep(20)
          
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


'''
+79228041539
'''