from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from pages.base_page import BasePage

def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_basket()
    page.should_press_add_basket()
    page.solve_quiz_and_get_code()
    page.check_name_of_product()
    
