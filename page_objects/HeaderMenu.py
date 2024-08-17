from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HeaderMenu:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_link_locator = (By.XPATH, "//a[@data-test='accountNav-signIn']")

    def click_sign_in_link(self):
        sign_in_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sign_in_link_locator)
        )
        sign_in_link.click()
