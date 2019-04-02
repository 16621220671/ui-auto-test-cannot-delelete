from selenium import webdriver
from Common.baseui import baseUI
import time
import os
from Common.Assert import Assertions

class Test_first_test_demo:

     def test_test_demo(self,driver):
        base=baseUI(driver)

        driver.get("http://192.168.60.132/#/login")

        base.send_keys('输入用户名',"//input[@name='username']",'admin')
        base.send_keys('输入密码', "//input[@name='password']", '123456')
        base.click('登陆', "(//span[contains(text(),'登录')])[1]")
        base.click('点击商品',"//span[contains(text(),'商品')]")
        base.click('测试',"//span[contains(text(),'添加商品')]")
        base.click('测试',"(//label[contains(text(),'商品分类：')]/following-sibling::div//span)[1]")
        base.click('测试',"//li[contains(text(),'手机数码')]")
        base.click('测试', "//li[contains(text(),'手机配件')]")
        base.send_keys('测试', "//label[contains(text(),'商品名称：')]/following-sibling::div//input", '耳机')
        base.send_keys('测试', "//label[contains(text(),'副标题：')]/following-sibling::div//input", '家hhhh用')
        base.click('测试', "//label[contains(text(),'商品品牌：')]/following-sibling::div//input")
        base.click('测试', "//span[contains(text(),'小米')]")

        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(1)

        base.click('测试', "//button/span[contains(text(),'下一步，填写商品促销')]")
        # base.send_keys('测试', "//label[contains(text(),'商品名称：')]/following-sibling::div//input", '耳机')

        base.click('测试', " // span[text() = '下一步，填写商品属性']")

        base.click('测试', " // span[text() = '下一步，选择商品关联']")

        base.click('测试', " // span[text() = '完成，提交商品']")

        base.click('测试', " // span[text() = '完成，提交商品']")

        base.click('测试', "//span[contains(text(),'   确定')]")



















