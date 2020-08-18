from page.page_login import *
import unittest
from selenium import webdriver


class Login_case(unittest.TestCase):
    '''登录页面的case'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get(url)
        self.login = Login_page(self.driver)
        self.login.click_account()

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def login_c(self, user, passw, title, expect):
        self.login.input_username(user)
        self.login.input_passw(passw)
        self.login.click_checkbox()
        self.login.submit()
        result = self.login.title_is(title)
        self.assertEqual(result, expect)

    def test_01(self):
        '''正确账号密码，登录成功'''
        self.login_c("cctv", "123456", "企业账户中心-首页", True)

    def test_02(self):
        '''正确账号错误密码，登录不成功'''
        self.login_c("cctv", "12345", "企业账户中心-首页", False)


if __name__ == "__main__":
    unittest.main()