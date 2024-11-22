from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from utils.locator import Locator

class ShoppingCartPage(Locator):
    def __init__(self, web: WebDriver):
        super().__init__(web)
        self.shopping_cart_button = lambda: self.web.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        self.shopping_cart_count = lambda: int(self.web.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]').text)
        self.products_in_cart = lambda : self.web.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item"]')
    
    def go_to_shopping_cart(self):
        self.shopping_cart_button().click()
        assert '/cart.html' in self.web.current_url
    
    def get_items_in_cart(self):
        items = self.items_in_cart()
        return len(items)