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
        # 记录第一条的编号//tbody/tr[1]/td[2]/div
        num = base.get_text('获取编号', "//tbody/tr[1]/td[2]/div")
        order_num = base.get_text("获取订单编号", "//tbody/tr[1]/td[3]/div")
        # 点击第一条订单发货//tbody/tr[1]/td[10]/div/button[3]
        base.click("点击第一条订单发货", "//tbody/tr[1]/td[10]/div/button[3]")
        # 点击配送方式//input[@placeholder='请选择物流公司']
        base.click("点击配送方式", "//input[@placeholder='请选择物流公司']")
        # 点击圆通快递//span[text()='圆通快递']
        base.click("点击圆通快递", "//span[text()='圆通快递']")
        # 输入物流单号//tbody/tr/td[7]//input
        base.send_keys("输入物流单号", "//tbody/tr/td[7]//input", "123456789")
        # 点击确定//span[text()='确定']
        base.click("点击确定", "//span[text()='确定']")
        # 确认(//span[contains(text(),'确定')])[2]
        base.click("确认", "(//span[contains(text(),'确定')])[2]")
        # 获取提示框文本//div[@role='alert']/p
        text = base.get_text("获取提示框文本", "//div[@role='alert']/p")
        # 断言
        assertions.assert_in_text(text, '发货成功')
        # 点击订单状态//label[contains(text(),'订单状态：')]/following-sibling::div//input
        base.click("点击订单状态", "//label[contains(text(),'订单状态：')]/following-sibling::div//input")
        # 点击已发货//span[text()='待发货']
        base.click("点击已发货", "//span[text()='已发货']")
        # 输入订单编号//input[@placeholder='订单编号']
        base.send_keys("输入订单编号", "//input[@placeholder='订单编号']", order_num)
        # 点击搜索查询//span[contains(text(),'查询搜索')]
        base.click("点击搜索查询", "//span[contains(text(),'查询搜索')]")
        # 定位到刚才发货的订单
        time.sleep(1)
        # 通过xpath定位到一组元素，存到一个list中
        nums = driver.find_elements_by_xpath("(//tbody)[1]/tr/td[2]")
        # 存放是否能找到编号 找到true  未找到 false
        b = False
        # 遍历上边的list
        for n in nums:
            # n.text取出元素的可视文本
            print(n.text)
            # 判断可视文本是否与发货订单的编号相同
            if n.text == num:
                # 如果相同，就讲true赋值给b
                b = True
        # 断言，订单状态转换是否正确
        assert True == b
        time.sleep(3)
