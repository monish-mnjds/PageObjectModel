from POM import *


class RegistrationPage(BasePage):
    RegistrationPage_Objects = read_locators("RegistrationPage")

    def select_male(self):
        locator_male = RegistrationPage.RegistrationPage_Objects['rdo_male']
        self.click_element(locator_male)

    def select_female(self):
        locator_female = RegistrationPage.RegistrationPage_Objects['rdo_female']
        self.click_element(locator_female)

    def enter_firstname(self, fname):
        locator_firstname = RegistrationPage.RegistrationPage_Objects['txt_firstname']
        self.enter_text(locator_firstname, value=fname)

    def enter_lastname(self, lname):
        locator_lastname = RegistrationPage.RegistrationPage_Objects['txt_lastname']
        self.enter_text(locator_lastname, value=lname)

    def enter_email(self, email):
        locator_email = RegistrationPage.RegistrationPage_Objects['txt_email']
        self.enter_text(locator_email, value=email)

    def enter_password(self, password):
        locator_password = RegistrationPage.RegistrationPage_Objects['txt_password']
        self.enter_text(locator_password, value=password)

    def enter_confirm_password(self, password):
        locator_confirm_password = RegistrationPage.RegistrationPage_Objects['txt_confirm_password']
        self.enter_text(locator_confirm_password, value=password)

    def click_register_button(self):
        locator_register = RegistrationPage.RegistrationPage_Objects['btn_register']
        self.click_element(locator_register)

    def verify_registration_successful(self):
        locator_register = RegistrationPage.RegistrationPage_Objects['lbl_reg_success']
        self.wait_for_element(locator_register)

