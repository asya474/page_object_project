from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_button_add_to_basket()
        self.add_product_to_button
    def should_be_product_url(self):
        assert self.is_element_present(self.browser.current_url), "Product url is not presented"
        assert True
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".btn-lg.btn-primary.btn-add-to-basket")
        assert True
    def add_product_to_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET) 
        button.click()
    def should_item_name_match(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_item_name = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        assert item_name == added_item_name
    def should_item_price_match(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        added_item_price = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_PRICE).text
        assert item_price == added_item_price
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
    def should_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
    