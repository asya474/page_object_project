from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(self.browser.current_url), "Login url is not presented"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Register form is not presented"
        assert True

    def register_new_user(self, link, email, password):
        link="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = 123456789
        time.sleep(10)
        email_form= self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        email_form.send_keys(email)
        password_form=self.browser.find_element(*LoginPageLocators.PASSWORD)
        password = str(time.time())
        password_form.send_keys(password)
        repeat_password_form=self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        repeat_password_form.send_keys(password)
        button_for_registration=self.browser.find_element(*LoginPageLocators.BUTTON_FOR_REGISTRATION)
        button_for_registration.click()