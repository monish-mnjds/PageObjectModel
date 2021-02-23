from POM import *


class LoginPage(BasePage):
    LoginPage_Objects = read_locators("LoginPage")

    def enter_email(self, email):
        locator_email = LoginPage.LoginPage_Objects['txt_email']
        self.enter_text(locator_email, value=email)

    def enter_password(self, password):
        locator_password = LoginPage.LoginPage_Objects['txt_password']
        self.enter_text(locator_password, value=password)

    def click_login_button(self):
        locator_login = LoginPage.LoginPage_Objects['btn_login']
        self.click_element(locator_login)
