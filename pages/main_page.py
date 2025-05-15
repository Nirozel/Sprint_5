from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    def go_to_post_ad_page(self):
        self.click(MainPageLocators.POST_AD_BUTTON)

    def is_user_avatar_visible(self):
        return self.is_element_visible(MainPageLocators.USER_AVATAR)

    def get_user_name(self):
        return self.get_element_text(MainPageLocators.USER_NAME)

    def logout(self):
        self.click(MainPageLocators.LOGOUT_BUTTON)

    def is_login_button_visible(self):
        return self.is_element_visible(MainPageLocators.LOGIN_BUTTON)