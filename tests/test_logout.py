import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestLogout:
    def test_successful_logout(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.go_to_login_page()
        login_page.go_to_registration()
        login_page.register_new_user()

        main_page.logout()

        assert main_page.is_login_button_visible()
        assert not main_page.is_user_avatar_visible()