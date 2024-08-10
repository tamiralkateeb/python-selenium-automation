from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.side_nav_sign_in_locator = (By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy'][normalize-space()='Sign in']")
        self.sign_in_form_locator = (By.XPATH, "//span[normalize-space()='Sign into your Target account']")
        self.login_button_locator = (By.XPATH, "//button[@id='login']")

    def click_side_nav_sign_in(self):
        wait = WebDriverWait(self.driver, 10)
        side_nav_sign_in = wait.until(EC.element_to_be_clickable(self.side_nav_sign_in_locator))
        side_nav_sign_in.click()

    def is_sign_in_form_visible(self):
        wait = WebDriverWait(self.driver, 10)
        sign_in_form = wait.until(EC.visibility_of_element_located(self.sign_in_form_locator))
        return sign_in_form.is_displayed()

    def is_login_button_visible(self):
        wait = WebDriverWait(self.driver, 10)
        login_button = wait.until(EC.visibility_of_element_located(self.login_button_locator))
        return login_button.is_displayed()
