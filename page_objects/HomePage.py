from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button_locator = (By.XPATH, "//a[@aria-label='Account, sign in']")
        self.search_box_locator = (By.ID, 'search')
        self.search_button_locator = (By.XPATH, "//button[@type='submit']")

    def click_sign_in(self):
        """Click on the Sign In button on the homepage."""
        sign_in_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sign_in_button_locator)
        )
        sign_in_button.click()

    def enter_search_term(self, search_term):
        """Enter a search term into the search box."""
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_box_locator)
        )
        search_box.clear()
        search_box.send_keys(search_term)

    def click_search_button(self):
        """Click the search button after entering a search term."""
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button_locator)
        )
        search_button.click()