import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.locators import AuthModalLocators, PostAdPageLocators


class TestPostCreation:
    def test_unauthenticated_user_cannot_create_post(self, driver):
        main_page = MainPage(driver)

        main_page.go_to_post_ad_page()

        modal_title = driver.find_element(*AuthModalLocators.MODAL_TITLE).text
        assert modal_title == "Чтобы разместить объявление, авторизуйтесь"

    def test_authenticated_user_can_create_post(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        # Register and login
        main_page.go_to_login_page()
        login_page.go_to_registration()
        login_page.register_new_user()
        time.sleep(1)
        main_page.go_to_post_ad_page()
        time.sleep(1)
        driver.find_element(*PostAdPageLocators.TITLE_INPUT).send_keys("Test Ad")
        driver.execute_script("window.scrollBy(0, 500);")
        driver.find_element(*PostAdPageLocators.DESCRIPTION_INPUT).send_keys("Test Description")
        driver.find_element(*PostAdPageLocators.PRICE_INPUT).send_keys("100")
        driver.find_element(*PostAdPageLocators.PUBLISH_BUTTON).click()
