from .product_page import ProductPage


def test_guest_should_add_product_to_cart_and_solve_quiz(browser):
    
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_added_product_to_cart()
