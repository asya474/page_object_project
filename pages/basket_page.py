from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def go_to_basket_page(self):
        link=self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()
    def should_not_to_be_added_items(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_ITEM_NAME), \
            "Added items are presented, but should not be"
    def should_be_basket_is_empty_message(self):
        assert self.is_element_present(*BasePageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "Basket is empty message is not presented, but should"
    