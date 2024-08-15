from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_result_locator = (By.XPATH, "//body/div[@id='__next']/div/main[@id='pageBodyContainer']/div[1]")

    def click_first_result(self):
        first_result = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_result_locator)
        )
        first_result.click()
