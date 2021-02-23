from POM import *
from Data import *


class BasePage(SeleniumWrapper):
    BasePage_Objects = read_locators("BasePage")

    def __init__(self, driver):
        super().__init__(driver)

    def click_register(self):
        register_locator = BasePage.BasePage_Objects['lnk_register']
        self.click_element(register_locator)

    def click_login_link(self):
        login_locator = BasePage.BasePage_Objects['lnk_login']
        self.click_element(login_locator)

    def verify_user_login(self, email):
        lnk_email = BasePage.BasePage_Objects['lnk_email']
        self.wait_for_element(("xpath", lnk_email[1].format(email)))

    def click_shopping_cart(self):
        lnk_shopping = BasePage.BasePage_Objects['lnk_shopping_cart']
        self.click_element(lnk_shopping)

    def enter_search_store(self, search_item):
        search_locator = BasePage.BasePage_Objects['txt_search_store']
        self.enter_text(search_locator, value=search_item)

    def click_books(self):
        locator = BasePage.BasePage_Objects['lnk_books']
        self.click_element(locator)

    def select_book(self, book):
        btn_add_cart = BasePage.BasePage_Objects['btn_add_cart']
        _xpath = btn_add_cart[1].format(book)
        locator = ("xpath", _xpath)
        self.click_element(locator)
