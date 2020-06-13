import pytest
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import time
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_button_add_to_basket()
    page.add_product_to_button()
    page.solve_quiz_and_get_code()
    page.should_item_name_match()
    page.should_item_price_match()
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_button()
    page.should_not_be_success_message()
def test_guest_cant_see_success_message(browser): 
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_button()
    time.sleep(1)
    page.should_success_message_is_disappeared()
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    basket_page=page.go_to_basket_page()
    basket_page=BasketPage(browser, link)
    basket_page.should_not_to_be_added_items()
    basket_page.should_be_basket_is_empty_message()
@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page=LoginPage(browser, link)
        page.open()
        page.register_new_user(link, email=str(time.time()) + "@fakemail.org", password=123456789)
        page.should_be_authorized_user()
        yield
    def test_user_cant_see_success_message(self, browser): 
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):   
        link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser,link)
        page.open()
        page.should_be_button_add_to_basket()
        page.add_product_to_button()
        page.solve_quiz_and_get_code()
        page.should_item_name_match()
        page.should_item_price_match()
       
    