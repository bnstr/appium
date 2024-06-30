from appium.webdriver.common.mobileby import MobileBy

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (MobileBy.ACCESSIBILITY_ID, "email")
        self.password_field = (MobileBy.ACCESSIBILITY_ID, "password")
        self.signup_button = (MobileBy.ACCESSIBILITY_ID, "signupButton")

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()
