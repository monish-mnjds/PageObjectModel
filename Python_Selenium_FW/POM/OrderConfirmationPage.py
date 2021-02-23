from POM import *


class OrderConfirmationPage(BasePage):
    OrderConfirmationPage_Objects = read_locators("OrderConfirmationPage")

    def click_order_details(self):
        ele_order_details = self.__class__.OrderConfirmationPage_Objects['lnk_order_details']
        self.click_element(ele_order_details)

    def click_pdf_invoice(self):
        ele_pdf = self.__class__.OrderConfirmationPage_Objects['lnk_pdf_invoice']
        self.click_element(ele_pdf)

    def verify_order_confirmation(self):
        txt_confirmation = self.__class__.OrderConfirmationPage_Objects['txt_order_confirmation']
        self.wait_for_element(txt_confirmation)
