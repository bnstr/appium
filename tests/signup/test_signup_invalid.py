import unittest
from utils.appium_setup import setup_appium
from page_objects.signup_page import SignupPage

class TestSignupInvalid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = setup_appium()
        cls.signup_page = SignupPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_invalid_signup(self):
        self.signup_page.enter_email("invalid_email")
        self.signup_page.enter_password("short")
        self.signup_page.click_signup()
        # Add assertions to verify failed signup

if __name__ == "__main__":
    unittest.main()
