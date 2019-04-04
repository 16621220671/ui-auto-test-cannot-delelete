from selenium import webdriver
from Common.baseui import baseUI
import time
import os
from Common.Assert import Assertions

class TestFirstUIDemo:
    def test_demo5(self, driver):
        assertions=Assertions()
        base = baseUI(driver)
        # 打开网址
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名//input[@name='username']
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        # 输入密码//input[@name='password']
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录(//span[contains(text(),'登录')])[1]
        base.click('点击登录', "(//span[contains(text(),'登录')])[1]")
        # 点击订单//span[text()='订单']
        base.click("点击订单", "//span[text()='订单']")
        # 点击订单列表(//span[text()='订单列表'])[1]
        base.click("点击订单列表", "(//span[text()='订单列表'])[1]")
        # 点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        # 点击待发货//span[text()='待发货']
        base.click("点击待发货", "//span[text()='待发货']")
        # 点击搜索查询//span[contains(text(),'查询搜索')]
        base.click("点击搜索查询", "//span[contains(text(),'查询搜索')]")
        base.scroll_screen("滚动窗口")

        base.click('选择全部订单', "//section//div//thead//span/span")
        base.click('批量操作', "//section/div/div[4]/div/div/input")


        base.click("批量发货", "//span[contains(text(),'批量发货')]")
        base.click("点击确定", "//span[contains(text(),'确定')]")
        rows = len(driver.find_elements_by_xpath("//tbody/tr"))
        for i in range(1,rows+1):

            base.click("点击选择物流公司","//tbody/tr[{0}]/td[6]//input".format(i))
            base.click("选择快递", "(//span[text()='中通快递'])[10]")
            base.send_keys("填写物流单号","//tbody/tr[{0}]/td[7]//input".format(i),'147852963')
            if i == 5 :
                base.scroll_screen("滚动窗口")


        base.click("点击确定", "(//span[contains(text(),'确定')])[1],'确定')]")
        base.click("点击确定", "(//span[contains(text(),'确定')])[2],'确定')]")
        time.sleep(2)
        text = base.get_text("获取提示框文本", "//div[@role='alert']/p")
        # 断言
        assertions.assert_in_text(text, '发货成功')






