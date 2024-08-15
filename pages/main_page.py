from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .login_page import LoginPage



class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link")


    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),'login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),'register form is not presented'

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

