from POM import *


class CartPage(BasePage):
    CartPage_Objects = read_locators("CartPage")

    def click_accept_terms_services(self):
        ele_chk_box = CartPage.CartPage_Objects['chk_terms']
        self.click_element(ele_chk_box)

    def click_checkout(self):
        ele_checkout = CartPage.CartPage_Objects['btn_checkout']
        self.click_element(ele_checkout)