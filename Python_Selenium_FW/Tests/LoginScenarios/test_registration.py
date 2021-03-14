from Tests import *
from POM import *

headers, data = read_data("Shopping", "test_registration")


@pytest.mark.parametrize(headers, data)
@pytest.mark.usefixtures("init")
class TestRegistration:
    def test_registration(self, fname, lname, email, password):
        rp = RegistrationPage(self.driver)
        rp.click_register()
        rp.select_male()
        rp.enter_firstname(fname)
        rp.enter_lastname(lname)
        rp.enter_email(email)
        rp.enter_password(password)
        rp.enter_confirm_password(password)
        rp.click_register_button()
        rp.verify_registration_successful()
