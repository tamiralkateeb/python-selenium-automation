from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_form_locator = (By.XPATH, "//span[normalize-space()='Sign into your Target account']")

    def is_sign_in_form_visible(self):
        sign_in_form = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.sign_in_form_locator)
        )
        return sign_in_form.is_displayed()
