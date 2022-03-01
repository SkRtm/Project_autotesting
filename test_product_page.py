from .product_page import ProductPage
import pytest


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


def test_success_message_not_presented_before_adding_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.shouldnt_be_success_message()
    product_page.add_to_cart()
    product_page.should_be_added_product_to_cart()