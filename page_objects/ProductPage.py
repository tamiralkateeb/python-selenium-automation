from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button_locator = (By.XPATH, "//div[@class='sc-529a2ea7-0 hbiLND']//div//button[@id='addToCartButtonOrTextIdFor90554775']")
        self.view_cart_button_locator = (By.XPATH, "//a[normalize-space()='View cart & check out']")

    def add_to_cart(self):
        """Add the product to the cart."""
        add_to_cart_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.add_to_cart_button_locator)
        )
        add_to_cart_button.click()

    def view_cart_and_checkout(self):
        """Click on 'View cart & check out'."""
        view_cart_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.view_cart_button_locator)
        )
        view_cart_button.click()
