import unittest
from utils.appium_setup import setup_appium
from page_objects.login_page import LoginPage

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = setup_appium()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_valid_login(self):
        self.login_page.enter_username("valid_username")
        self.login_page.enter_password("valid_password")
        self.login_page.click_login()
        # Add assertions to verify successful login

if __name__ == "__main__":
    unittest.main()
