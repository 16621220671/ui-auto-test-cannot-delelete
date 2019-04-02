#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



def shot(func):
    def function(*args, **kwargs):
        allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之前', allure.attachment_type.PNG)

        func(*args, **kwargs)
        allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之后', allure.attachment_type.PNG)

    return function


class baseUI():

    def __init__(self,driver):
        self.driver = driver

    def local_element(self,xpath):
       return WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH,xpath)))

    @shot
    def send_keys(self,step,xpath,text):
        element = self.local_element(xpath)
        element.clear()
        element.send_keys(text)


    @shot
    def click(self,step,xpath):
        element = self.local_element(xpath)
        element.click()
    @shot
    def scroll_screen(self,step):
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)