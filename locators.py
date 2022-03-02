from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_OF_PRODUCT_ADDED_TO_CART = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    TOTAL_PRICE_OF_CART = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    CART_LINK = (By.CSS_SELECTOR, ".btn-group > a")


class BasketPageLocators:
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "p > a")
    PRODUCTS_IN_CART = (By.CSS_SELECTOR, ".col-sm-6.h3")
