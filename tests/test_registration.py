import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestRegistration:
    def test_successful_registration(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_login_page()
        login_page.go_to_registration()
        login_page.register_new_user()

        assert main_page.is_user_avatar_visible()
        assert main_page.get_user_name() == "User."

    def test_registration_with_invalid_email(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_login_page()
        login_page.go_to_registration()
        login_page.register_with_invalid_email("invalid_email")

        assert login_page.is_error_message_visible()

    def test_registration_existing_user(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_login_page()
        login_page.go_to_registration()
        email = login_page.register_new_user()
        main_page.logout()
        main_page.go_to_login_page()
        login_page.go_to_registration()
        login_page.register_new_user(email=email, password="Test1234")

        assert login_page.is_error_message_visible()
