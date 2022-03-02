from .product_page import ProductPage
from .basket_page import BasketPage
from .login_page import LoginPage
import pytest
import time

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope = "function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.shouldnt_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_cart()
        product_page.should_be_added_product_to_cart()


def test_guest_should_add_product_to_cart_and_solve_quiz(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_added_product_to_cart()


@pytest.mark.parametrize('parameter', [n if n != 7 else pytest.param(n, marks = pytest.mark.xfail) for n in range(10)])
def test_find_bug_promo_action(browser, parameter):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{parameter}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_added_product_to_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.shouldnt_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.shouldnt_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_disappear_success_message()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_cart()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.shouldnt_be_products_in_basket()
    basket_page.should_be_empty_basket()