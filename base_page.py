from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

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
            return False

        return True
