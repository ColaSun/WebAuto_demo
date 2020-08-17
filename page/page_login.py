from common.base import Base
url = "https://www.tobosu.com/passport/login.html"

class Login_page(Base):
    account = ("css selector", ".normal")
    user = ("id", "username")
    passw = ("id", "password")
    checkbox = ("css selector", "[class='autologin']")
    forgetpassw = ("link text", "忘记密码?")
    login = ("class name", "usernameLogin")
    register = ("link text", "立即注册")

    def click_account(self):
        '''点击账户登录'''
        self.click(self.account)

    def input_username(self, text):
        '''输入账号'''
        self.send_keys(self.user, text)

    def input_passw(self, text):
        '''输入密码'''
        self.send_keys(self.passw, text)

    def submit(self):
        '''点击登录'''
        self.click(self.login)

    def click_checkbox(self):
        '''点击记住密码'''
        self.click(self.checkbox)

    def click_forgetpassw(self):
        '''点击忘记密码'''
        self.click(self.forgetpassw)

    def click_register(self):
        '''点击立即注册'''
        self.click(self.register)

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get(url)
    login = Login_page(driver)
    login.click_account()
    login.click_forgetpassw()
    driver.back()
    login.click_account()
    login.click_register()
    driver.back()
    login.click_account()
    login.input_username("cctv")
    login.input_passw("123456")
    login.click_checkbox()
    login.submit()
