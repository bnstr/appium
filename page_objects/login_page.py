from appium.webdriver.common.mobileby import MobileBy

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (MobileBy.ACCESSIBILITY_ID, "username")
        self.password_field = (MobileBy.ACCESSIBILITY_ID, "password")
        self.login_button = (MobileBy.ACCESSIBILITY_ID, "loginButton")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
