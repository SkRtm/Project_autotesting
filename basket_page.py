from unittest.mock import Base
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def shouldnt_be_products_in_basket(self):
        assert self.is_not_element_presented(*BasketPageLocators.PRODUCTS_IN_CART),\
            "You already have some products in your cart"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), \
            "There is no message about empty basket"