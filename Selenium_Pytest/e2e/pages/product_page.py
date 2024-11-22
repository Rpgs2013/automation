from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriver
from utils.locator import Locator


class ProductListPage(Locator):
    
    def __init__(self, web: WebDriver, product: WebElement):
        super().__init__(web)
        self.product = product

        self.add_to_cart_button = lambda: self.product(By.CSS_SELECTOR, '.data-test="add-to-cart"')
        self.product_price = lambda: int(self.product.find_element(By.CSS_SELECTOR, '.inventory_item_price').text.replace('$', ''))

def add_to_cart(self):
    self.add_to_cart_button().click()