from selenium import webdriver
from Common.baseui import baseUI
import time
import os
from Common.Assert import Assertions


class Test_first_test_demo:

    def test_test_demo(self, driver):
        base = baseUI(driver)

        driver.get("http://192.168.60.132/#/login")
        base.send_keys('输入用户名', "//input[@name='username']", 'admin')
        base.send_keys('输入密码', "//input[@name='password']", '123456')
        base.click('登陆', "(//span[contains(text(),'登录')])[1]")

        base.click('点击营销', "//span[contains(text(),'营销')]")
        base.click('点击优惠券列表', "//span[contains(text(),'优惠券列表')]")
        base.click('点击编辑', "//span[contains(text(),'编辑')]")


        base.send_keys('输入优惠券名称', "//label[contains(text(),'优惠券名称：')]/following-sibling::div//input", '通用')

        base.send_keys('总发行量', "//label[contains(text(),'总发行量：')]/following-sibling::div//input", '200')
        base.send_keys('面额', "//label[contains(text(),'面额：')]/following-sibling::div//input", '1000')
        base.send_keys('使用门槛', "//label[contains(text(),'使用门槛')]/following-sibling::div//input", '50')

        base.click('点击提交', "//span[contains(text(),'提交')]")

        base.click('点击确认', "//span[contains(text(),'确定')]")

        # print(driver.page_source)
        xpatha = driver.find_element_by_xpath("//div[contains(@role,'alert')]/p ")
        # print(xpath.text)
        Assertions.assert_in_text(xpatha.text, '修改成功')











