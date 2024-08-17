from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        # This locator should be the actual cart icon you are trying to click
        self.cart_icon_locator = (By.CSS_SELECTOR, "a[aria-label='cart 1 items']")
        self.cart_item_locator = (By.XPATH, "//span[@data-test='item-count']")

    def open_cart(self):
        """Click the cart icon to open the cart."""
        cart_icon = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.cart_icon_locator)
        )
        cart_icon.click()

    def get_cart_item_count(self):
        """Get the number of items in the cart."""
        cart_item = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.cart_item_locator)
        )
        return cart_item.text
