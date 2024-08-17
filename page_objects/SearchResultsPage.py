from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        # Locator for the Mug Root Beer product
        self.product_locator = (By.XPATH, "//body/div[@id='__next']/div/main[@id='pageBodyContainer']/div/div[1]")

    def click_first_product(self):
        """Click on the first product in the search results."""
        product = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.product_locator)
        )
        product.click()
