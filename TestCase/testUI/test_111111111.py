from selenium import webdriver
from Common.baseui import baseUI
import time
import os
from Common.Assert import Assertions


class Test_first_test_demo3:

    def test_test_demo3(self, driver):
        base = baseUI(driver)
        assertions = Assertions()

        driver.get("http://192.168.60.132/#/login")
        base.send_keys('输入用户名', "//input[@name='username']", 'admin')
        base.send_keys('输入密码', "//input[@name='password']", '123456')
        base.click('登陆', "(//span[contains(text(),'登录')])[1]")
        # 点击订单
        base.click('订单', "//span[contains(text(),'订单')]")
        # 点击订单列表
        base.click('订单列表', "//span[contains(text(),'订单列表')]")
        # 订单状态
        base.click('订单状态', "//label[contains(text(),'订单状态')]/following-sibling::div//input")
        # 选择待发货
        base.click('待发货', "//span[contains(text(),'待发货')]")

        # 点击查询搜索
        base.click('查询搜索', "//span[contains(text(),'查询搜索')]")
        # 点击订单发货
        base.click('订单发货', "(//span[contains(text(),'订单发货')])[1]")
        xpatha = driver.f("(//tbody//div)[1]")
        print('订单编号:',xpatha)
        #
        # # 点击确认
        # base.click('确认', "//span[contains(text(),'确定')]")
        # # 点击提示中确认
        # base.click('确认', "//span[contains(text(),'确定')]")
        # # 查看刚待发货的订单发货状态是否已经更改















