from .base_page import BasePage
from .locators import ProductPageLocators
from math import log, sin
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):

    def solve_quiz_and_get_code(self): #решает уравнение из окошка alert
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
             alert = self.browser.switch_to.alert
             alert_text = alert.text
             print(f"Your code: {alert_text}")
             alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_cart(self): 
        #добавляет товар в корзину
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_the_same_name_of_product_added_to_cart_and_product(self): \
        #сравнивает имя товара и имя товара в корзине
        product_name = self.browser.\
            find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        product_name_added_to_cart = self.browser.\
            find_element(*ProductPageLocators.NAME_OF_PRODUCT_ADDED_TO_CART).text
        assert product_name == product_name_added_to_cart,\
            f"Names of products are not the same. Expected {product_name} instead of {product_name_added_to_cart}"
    
    def should_be_the_same_price_of_cart_and_product(self):
        #сравнивает цену товара и цену товара в корзине
        product_price = self.browser.\
            find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        price_of_cart = self.browser.\
            find_element(*ProductPageLocators.TOTAL_PRICE_OF_CART).text
        assert product_price == price_of_cart, \
            f"Prices of products are not the same. Expected {product_price} instead of {price_of_cart}"

    def should_be_added_product_to_cart(self):
        #объединение функций на сравнение цен и имен товара в одну
        #если какая-лбо из функций не пройдет assert, выполнение этой функции прекратится
        self.should_be_the_same_name_of_product_added_to_cart_and_product()
        self.should_be_the_same_price_of_cart_and_product()

    def shouldnt_be_success_message(self):
        assert self.is_not_element_presented(*ProductPageLocators.NAME_OF_PRODUCT_ADDED_TO_CART), \
            "Success message is presented before product added to cart"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message doesnt disappear"