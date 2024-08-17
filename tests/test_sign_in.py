import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.HomePage import HomePage
from page_objects.HeaderMenu import HeaderMenu
from page_objects.SignInPage import SignInPage

class TestSignIn(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.target.com/")
        self.driver.maximize_window()

    def test_sign_in_access(self):
        home_page = HomePage(self.driver)
        home_page.click_sign_in()

        header_menu = HeaderMenu(self.driver)
        header_menu.click_sign_in_link()

        sign_in_page = SignInPage(self.driver)
        self.assertTrue(sign_in_page.is_sign_in_form_visible(), "Sign In form was not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
