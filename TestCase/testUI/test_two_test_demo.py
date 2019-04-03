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
        base.click('点击商品', "//span[contains(text(),'商品')]")
        base.click('添加商品', "(//span[text() = '添加商品'])[1]")
        base.click('测试', "(//label[contains(text(),'商品分类：')]/following-sibling::div//span)[4]")
        base.click('测试', "//li[contains(text(),'手机数码')]")
        base.click('测试', "//li[contains(text(),'手机配件')]")

        base.send_keys('测试', "//label[contains(text(),'商品名称：')]/following-sibling::div//input", '耳io机')
        base.send_keys('测试', "//label[contains(text(),'副标题：')]/following-sibling::div//input", '家hohhh用')
        base.click('测试', "//label[contains(text(),'商品品牌：')]/following-sibling::div//input")
        base.click('测试', "//span[contains(text(),'小米')]")

        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(2)

        base.click('测试', "//span[contains(text(),'下一步，填写商品促销')]")
        base.click('测试', "//span[contains(text(),'下一步，填写商品属性')]")

        base.click('属性类型', "//label[contains(text(), '属性类型：')] /following-sibling::div/div/div")
        base.click('配件', "//span[text()='配件']")
        base.click('电脑详情', "(// label[contains(text(), '规格参数：')] /following-sibling::div/div/div/div/div/div/div)[1]")
        xpath = driver.find_element_by_xpath("(//iframe[contains(@id,'vue-tinymce')])[1]")
        driver.switch_to_frame(xpath)
        # 填写规格参数
        base.send_keys("填写规格参数", "//body[@id='tinymce']", "一桌晶")
        driver.switch_to_default_content()

        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)

        base.click('下一步,选择商品关联', "//span[contains(text(),'下一步，选择商品关联')]")
        base.click('测试', "//span[text() = '完成，提交商品']")
        base.click('提示', "//span[contains(text(),'取消')]")


