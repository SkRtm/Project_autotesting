from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators

class BasePage:

    def __init__(self, browser, url, timeout = 5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        
        except NoSuchElementException:
            return False

        return True

    def is_not_element_presented(self, method, locator, timeout = 4):
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            return True

        return False


    def is_disappeared(self, method, locator, timeout = 4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            return False
        
        return True

    
    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
    

    def should_be_login_link(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_LINK),\
            "Login link isnt presented here"