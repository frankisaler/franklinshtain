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

class out(unittest.TestCase):
    def outlook_setUp(self):
        self.person = jload()
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://outlook.live.com/owa/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def outlook_start(self):
        driver = self.driver
        driver.get("https://outlook.live.com/owa/")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Free Outlook email and calendar'])[2]/following::span[1]").click()
        driver.find_element_by_id("MemberName").clear()
        sleep(3)
        tp2(self.person['login'])
        press('tab')
        press('tab')
        press('enter')
        driver.find_element_by_id("PasswordInput").clear()
        mt(x=436, y=396)
        tp2(self.person['password'])
        driver.find_element_by_id("iSignupAction").click()
        driver.find_element_by_id("FirstName").clear()
        sleep(3)
        mt(x=398, y=441)
        tp2(self.person['first'])
        sleep(3)
        mt(x=391, y=495)
        tp2(self.person['last'])
        driver.find_element_by_id("iSignupAction").click()
        driver.find_element_by_id("BirthMonth").click()
        sleep(3)
        Select(driver.find_element_by_id("BirthMonth")).select_by_visible_text(self.person['mounth'].title())
        driver.find_element_by_id("BirthMonth").click()
        driver.find_element_by_id("BirthDay").click()
        sleep(3)
        Select(driver.find_element_by_id("BirthDay")).select_by_visible_text(self.person['day'])
        driver.find_element_by_id("BirthDay").click()
        driver.find_element_by_id("BirthYear").click()
        sleep(3)
        Select(driver.find_element_by_id("BirthYear")).select_by_visible_text(self.person['year'])
        driver.find_element_by_id("iSignupAction").click()
        sleep(6)
        screenshot(r'temp\1.png', region=(354, 396, 180, 80))
        s3 = boto3.client('s3')
        s3.upload_file(r'temp\1.png', 'franki', '1.png', ExtraArgs={'ACL': 'public-read'})
        captch = captcha('https://hb.bizmrg.com/franki/1.png')
        answer = captch['solution']['text']
        look = r'[\S]+'
        fv = findall(look, answer)
        lenfv = len(fv)
        if lenfv == 2:
            answ = fv[0] + fv[1]
        else:
            answ = fv[0]
        mt(x=602, y=507)
        tp(answ)
        services = 'outlook.json'
        write_json(services)
        sleep(20)
        driver.close()
    
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
