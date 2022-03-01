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
    #за success_message принят блок из трех сообщений:
    #товар добавлен в корзину
    #корзина удовлетворяет Shipping Offer
    #стоимость корзины составляет ...
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages")
