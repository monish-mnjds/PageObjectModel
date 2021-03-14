from POM import *
from Tests import *


headers, data = read_data("Shopping", "test_shopping")


@pytest.mark.usefixtures("init")
@pytest.mark.parametrize(headers, data)
class TestShopping:
    def test_shopping(self, email, password, fname, lname, country, city,
                   add1, add2, zip_code, phone, po_number):
        lp = LoginPage(self.driver)

        # Click on Login Link
        lp.click_login_link()

        # Login into shopping cart
        lp.enter_email(email)
        lp.enter_password(password)
        lp.click_login_button()

        # Click on Books link
        lp.click_books()

        # Click on Add Cart button of Health Book
        lp.select_book("Health Book")

        # Click on Shopping Cart Link
        lp.click_shopping_cart()

        # Accept terms and Conditions and Click on Checkout
        cp = CartPage(self.driver)
        cp.click_accept_terms_services()
        cp.click_checkout()

        # Enter Billing Address
        cop = CheckOutPage(self.driver)
        cop.select_new_address()
        cop.enter_first_name(fname)
        cop.enter_last_name(lname)
        cop.enter_email(email)
        cop.select_country(country)
        cop.enter_city(city)
        cop.enter_add_line1(add1)
        cop.enter_add_line2(add2)
        cop.enter_zip_code(zip_code)
        cop.enter_phone(phone)

        # Click on Continue
        cop.click_continue_billing_address()

        # Click on Store Pickup
        cop.click_store_pickup()

        # Click on Continue
        cop.click_continue_shipping()

        # Click Purchase Order
        cop.select_purchase_order()

        # Click Continue Payment
        cop.click_continue_payment()

        # Enter PO Number
        cop.enter_po_number(po_number)

        # Click Continue
        cop.click_continue_payment_info()

        # Click on Confirm
        cop.click_confirm()

        # Verify Order Successful Message
        ocp = OrderConfirmationPage(self.driver)

        ocp.verify_order_confirmation()

        # Click Order Details
        ocp.click_order_details()

        # Click PDF Invoice
        ocp.click_pdf_invoice()
