from pages.base_page import BasePage
from locators.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def is_ad_visible(self, ad_title):
        ads = self.driver.find_elements(*ProfilePageLocators.AD_ITEM)
        for ad in ads:
            if ad_title in ad.text:
                return True
        return False