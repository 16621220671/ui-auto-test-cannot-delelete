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




        #base.send_keys("上传文件","//input[@type='file']","‪D:/1.png")
        #删除日期控件，只读属性
        #base.remove_attribute_by_xpath("删除日期控件，只读属性","//input[@type='date']","readonly")
        # base.update_attribute_by_xpath("修改日期控件value值","//input[@type='date']",'value','2019-04-03')
        # base.select_by_visible_text("选择丁雁玲","//select","丁雁玲")
        # time.sleep(1)
        # base.select_by_value("选择魏谦","//select","w")
        # time.sleep(1)
        # base.select_by_index("选择丁雁玲","//select",1)
        # select = Select(driver.find_element_by_xpath("//select"))
        # select.select_by_visible_text("丁雁玲")
        # time.sleep(1)
        # select.select_by_index(2)
        # time.sleep(1)
        # select.select_by_value("d")
        #base.click("点击百度","//a[contains(text(),'百度')]")
        # action = ActionChains(driver)
        # action.key_down(Keys.CONTROL).click(driver.find_element_by_xpath("//a[contains(text(),'百度')]")).key_up(Keys.CONTROL).perform()
        # time.sleep(3)
        # action.key_down(Keys.SHIFT).click(driver.find_element_by_xpath("//a[contains(text(),'百度')]")).key_up(Keys.SHIFT).perform()
        # time.sleep(5)


