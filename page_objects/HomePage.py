from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box_locator = (By.ID, 'search')
        self.search_button_locator = (By.XPATH, "//button[@type='submit']")

    def enter_search_term(self, search_term):
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_box_locator)
        )
        search_box.clear()
        search_box.send_keys(search_term)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button_locator)
        )
        search_button.click()
