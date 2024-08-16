from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID,'login_form')
    REGISTER_FORM = (By.ID,'register_form')

class AddToBasketLocators():
    ADD_TO_BASKET = (By.CLASS_NAME,'btn-lg')
    CHECKING_MASAGE = (By.XPATH,"//div[contains(text(), 'basket')]")
    CHECK_THE_BOOK = (By.XPATH,'//div[class="alertinner"]/strong')
    THE_BOOK = (By.CLASS_NAME,'product_main')
    # THE_PRICE_OF_BOOK = (By.CLASS_NAME,'price_color')
    # THE_BUSKET_TOTAL = (By.CLASS_NAME,'')

