import unittest
from utils.appium_setup import setup_appium
from page_objects.login_page import LoginPage

class TestLoginInvalid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = setup_appium()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_invalid_login(self):
        self.login_page.enter_username("invalid_username")
        self.login_page.enter_password("invalid_password")
        self.login_page.click_login()
        # Add assertions to verify failed login

if __name__ == "__main__":
    unittest.main()
