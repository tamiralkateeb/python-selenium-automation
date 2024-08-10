from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button_locator = (By.XPATH, "//a[@aria-label='Account, sign in']")
        self.cart_icon_locator = (By.XPATH, "//a[@aria-label='cart 0 items']")

    def click_sign_in(self):
        wait = WebDriverWait(self.driver, 10)
        sign_in_button = wait.until(EC.element_to_be_clickable(self.sign_in_button_locator))
        sign_in_button.click()

    def click_cart_icon(self):
        wait = WebDriverWait(self.driver, 10)
        cart_icon = wait.until(EC.element_to_be_clickable(self.cart_icon_locator))
        cart_icon.click()
