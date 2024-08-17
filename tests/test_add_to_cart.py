from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

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

# SearchResultsPage class
class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_result_locator = (By.XPATH, "//body/div[@id='__next']/div/main[@id='pageBodyContainer']/div[1]")

    def click_first_result(self):
        first_result = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_result_locator)
        )
        first_result.click()


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button_locator = (By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > main:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")

    def add_to_cart(self):
        # Wait until the button is visible and clickable
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.add_to_cart_button_locator)
        )
        add_to_cart_button.click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon_locator = (By.CSS_SELECTOR, "a[aria-label='cart 1 items']")
        self.cart_item_locator = (By.XPATH, "//span[@data-test='item-count']")

    def open_cart(self):
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon_locator)
        )
        cart_icon.click()

    def get_cart_item_count(self):
        cart_item = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.cart_item_locator)
        )
        return cart_item.text

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.target.com/")
        self.driver.maximize_window()

    def test_add_product_to_cart(self):

        home_page = HomePage(self.driver)
        home_page.enter_search_term("mug root beer")
        home_page.click_search_button()

        search_results_page = SearchResultsPage(self.driver)
        search_results_page.click_first_result()

        product_page = ProductPage(self.driver)
        product_page.add_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.open_cart()
        item_count = cart_page.get_cart_item_count()

        self.assertEqual(item_count, "1", "Item was not added to the cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
