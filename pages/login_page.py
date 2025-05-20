import uuid
from pages.base_page import BasePage
from locators.locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_registration(self):
        self.click(LoginPageLocators.NO_ACCOUNT_BUTTON)

    def register_new_user(self, email=None, password="Test1234"):
        if email is None:
            email = f"test_{uuid.uuid4().hex[:6]}@example.com"

        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.send_keys(LoginPageLocators.CONFIRM_PASSWORD_INPUT, password)
        self.click(LoginPageLocators.CREATE_ACCOUNT_BUTTON)
        return email

    def login(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def is_error_message_visible(self):
        return self.is_element_visible(LoginPageLocators.ERROR_MESSAGE)

    def register_with_invalid_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.click(LoginPageLocators.CREATE_ACCOUNT_BUTTON)
