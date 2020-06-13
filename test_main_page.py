from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/" 
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/" 
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def should_be_login_link(self):
    assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
#в методе, который осуществляет переход к странице логина, проинициализировать новый объект Page и вернуть его:
def test_guest_can_go_to_login_page(browser):
   link = "http://selenium1py.pythonanywhere.com"
   page = MainPage(browser, link)
   page.open()
   login_page = page.go_to_login_page()
   login_page=LoginPage(browser, link)
   login_page.should_be_login_link()
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    basket_page=page.go_to_basket_page()
    basket_page=BasketPage(browser, link)
    basket_page.should_not_to_be_added_items()
    basket_page.should_be_basket_is_empty_message()