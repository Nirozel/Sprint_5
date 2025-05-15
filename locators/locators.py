from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    POST_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    USER_AVATAR = (By.CSS_SELECTOR, '.circleSmall')
    USER_NAME = (By.CSS_SELECTOR, ".name")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")


class LoginPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT = (By.NAME, "email")
    EMAIL_INPUT_ERROR = (By.CSS_SELECTOR, '#root > div > div.homePage_homepageStyle__WP-Y1 > div.homePage_modal__zSdUB > form > div.popUp_inputColumn__RgD8n > div:nth-child(1) > div > div')
    PASSWORD_INPUT = (By.NAME, "password")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".input_span__yWPqB")
    ERROR_FIELD = (By.CSS_SELECTOR, ".error-field")


class ProfilePageLocators:
    MY_ADS_SECTION = (By.CSS_SELECTOR, ".my-ads")
    AD_ITEM = (By.CSS_SELECTOR, ".ad-item")


class PostAdPageLocators:
    TITLE_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/textarea")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.NAME, "category")
    CITY_DROPDOWN = (By.NAME, "city")
    CONDITION_RADIO = (By.NAME, "condition")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")


class AuthModalLocators:
    MODAL_TITLE = (By.CSS_SELECTOR, "#root > div > div.homePage_homepageStyle__WP-Y1 > div.homePage_modal__zSdUB > form > div.popUp_titleRow__M7tGg > h1")