from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import AddToBasketLocators
from pages import base_page


class ProductPage(BasePage):
    def should_be_add_basket(self):
        assert self.is_element_present(By.CLASS_NAME, "btn-lg")

    def should_press_add_basket(self):
        button2 = self.browser.find_element(*AddToBasketLocators.ADD_TO_BASKET)
        button2.click()

    def check_name_of_product(self):
        assert self.is_element_present(*AddToBasketLocators.CHECKING_MASAGE)
        # book = self.browser.find_element(*AddToBasketLocators.THE_BOOK)
        # prod = self.browser.find_element(*AddToBasketLocators.CHECK_THE_BOOK)
        # assert prod == book, 'the book name is not the same'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*AddToBasketLocators.CHECKING_MASAGE), \
        "Success message is presented, but should not be"
    
    def should_see_element_disappeard(self):
        assert self.is_disappeared(*AddToBasketLocators.CHECKING_MASAGE), \
        "Success message is presented, but should not be"
    
