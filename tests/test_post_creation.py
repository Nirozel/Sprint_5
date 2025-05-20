import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.base_page import BasePage

class TestPostCreation:
    def test_unauthenticated_user_cannot_create_post(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_post_ad_page()
        main_page.modal_title()
        assert main_page.modal_title() == "Чтобы разместить объявление, авторизуйтесь"

    def test_authenticated_user_can_create_post(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        base_page = BasePage(driver)
        main_page.go_to_login_page()
        login_page.go_to_registration()
        login_page.register_new_user()
        assert main_page.is_user_avatar_visible()
        main_page.go_to_post_ad_page()
        main_page.ad_title("Test Ad")
        base_page.scroll_down()
        main_page.ad_description("Test Description")
        main_page.ad_price("100")
        main_page.publicate_button()
        base_page.scroll_up()
        assert main_page.is_user_avatar_visible()
