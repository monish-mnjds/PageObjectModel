from Tests import *
from POM import *

headers, data = read_data("Shopping", "test_login")


@pytest.mark.usefixtures("init")
@pytest.mark.parametrize(headers, data)
class TestLogin:
    def test_login(self, email, password):
        lp = LoginPage(self.driver)

        # Click on Login Link
        lp.click_login_link()

        # Enter Username and Password
        lp.enter_email(email)
        lp.enter_password(password)

        # Click on Login
        lp.click_login_button()

        # Verify User login
        lp.verify_user_login(email)
