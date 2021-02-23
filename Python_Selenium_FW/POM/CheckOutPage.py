from POM import *


class CheckOutPage(BasePage):
    CheckOutPage_Objects = read_locators("CheckOutPage")

    def select_new_address(self):
        ele_address = CheckOutPage.CheckOutPage_Objects['lst_new_address']
        self.select_list_item(ele_address, item="New Address")

    def enter_first_name(self, fname):
        ele_fname = CheckOutPage.CheckOutPage_Objects['txt_first_name']
        self.enter_text(ele_fname, value=fname)

    def enter_last_name(self, lname):
        ele_lname = CheckOutPage.CheckOutPage_Objects['txt_last_name']
        self.enter_text(ele_lname, value=lname)

    def enter_email(self, email):
        ele_email = CheckOutPage.CheckOutPage_Objects['txt_email']
        self.enter_text(ele_email, value=email)

    def select_country(self, country):
        ele_country = CheckOutPage.CheckOutPage_Objects['lst_country']
        self.select_list_item(ele_country, item=country)

    def enter_city(self, city):
        ele_city = CheckOutPage.CheckOutPage_Objects['txt_city']
        self.enter_text(ele_city, value=city)

    def enter_add_line1(self,add1):
        ele_add1 = CheckOutPage.CheckOutPage_Objects['txt_add1']
        self.enter_text(ele_add1, value=add1)

    def enter_add_line2(self, add2):
        ele_add2 = CheckOutPage.CheckOutPage_Objects['txt_add2']
        self.enter_text(ele_add2, value=add2)

    def enter_zip_code(self, zip):
        ele_zip = CheckOutPage.CheckOutPage_Objects['txt_zip_code']
        self.enter_text(ele_zip, value=zip)

    def enter_phone(self, phone):
        ele_phone = CheckOutPage.CheckOutPage_Objects['txt_phone']
        self.enter_text(ele_phone, value=phone)

    def click_continue_billing_address(self):
        ele_shopping = CheckOutPage.CheckOutPage_Objects['btn_continue_billing_address']
        self.click_element(ele_shopping)

    def click_store_pickup(self):
        ele_store = CheckOutPage.CheckOutPage_Objects['chk_store_pickup']
        self.click_element(ele_store)

    def click_continue_shipping(self):
        ele_shopping = CheckOutPage.CheckOutPage_Objects['btn_continue_shipping']
        self.click_element(ele_shopping)

    def select_purchase_order(self):
        ele_pop = CheckOutPage.CheckOutPage_Objects['rdo_purchase_order']
        self.click_element(ele_pop)

    def click_continue_payment(self):
        ele_continue = CheckOutPage.CheckOutPage_Objects['btn_continue_payment']
        self.click_element(ele_continue)

    def enter_po_number(self, number):
        ele_po = CheckOutPage.CheckOutPage_Objects['txt_po_number']
        self.enter_text(ele_po, value=number)

    def click_continue_payment_info(self):
        ele_confirm = CheckOutPage.CheckOutPage_Objects['btn_continue_payment_info']
        self.click_element(ele_confirm)

    def click_confirm(self):
        ele_confirm = CheckOutPage.CheckOutPage_Objects['btn_confirm']
        self.click_element(ele_confirm)
