import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestLogin:
    def test_successful_login(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_login_page()
        login_page.go_to_registration()
        email = login_page.register_new_user()

        main_page.logout()

        main_page.go_to_login_page()
        login_page.login(email, "Test1234")

        assert main_page.is_user_avatar_visible()
        assert main_page.get_user_name() == "User."