from .base_page import BasePage
from selenium.webdriver.common.by import By



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(By.ID,'login_link')
        assert "login" in self.browser.current_url,'should be "login" in curent url'
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(By.ID,'login_form')

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(By.ID,'register_form')