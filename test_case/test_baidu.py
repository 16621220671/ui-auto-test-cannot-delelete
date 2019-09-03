

from Common.baseui import baseUI


class Test_first_test_demo:
    def test_test_demo(self,driver):
        base = baseUI(driver)
        driver.get('https://www.baidu.com/')
