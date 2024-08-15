import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.HomePage import HomePage
from page_objects.SearchResultsPage import SearchResultsPage

class TargetSearchTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.target.com/")
        self.driver.maximize_window()

    def test_search_for_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_search_term("laptop")
        home_page.click_search_button()

        search_results_page = SearchResultsPage(self.driver)
        search_results_page.click_first_result()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
