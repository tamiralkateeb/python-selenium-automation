from behave import given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I open the Target Circle page')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get("https://www.target.com/circle")
    context.driver.maximize_window()

@then('I should see exactly 10 benefit cells')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    # Assuming benefit cells have a unique CSS selector, update this as needed
    benefit_cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"cell-item-content")))
    assert len(benefit_cells) == 10, f"Expected 10 benefit cells, but found {len(benefit_cells)}"
    context.driver.quit()
