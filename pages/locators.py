from selenium.webdriver.common.by import By
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK=(By.CSS_SELECTOR, "#default  header div.page_inner div div.basket-mini.pull-right.hidden-xs  span a")
    BASKET_IS_EMPTY_MESSAGE=( By.CSS_SELECTOR, "#content_inner")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM =(By.CSS_SELECTOR, "#login_form" )
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM=(By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD=(By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD=(By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_FOR_REGISTRATION=(By.CSS_SELECTOR, "#register_form  button") 
class ProductPageLocators():
    ADD_TO_BASKET=(By.CSS_SELECTOR, ".btn-lg.btn-primary.btn-add-to-basket")
    ITEM_NAME=(By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ADDED_ITEM_NAME=(By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")
    ITEM_PRICE=(By.CSS_SELECTOR, ".col-sm-6.product_main p")
    ADDED_ITEM_PRICE=(By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon.alert-info.fade.in  p:nth-child(1) strong")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, "#messages :nth-child(1) ")

