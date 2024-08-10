from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I open the Target website for sign in')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get("https://www.target.com/")
    context.driver.maximize_window()

@when('I click on the Sign In button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Account, sign in']")))
    sign_in_button.click()

@when('I click on the Sign In link from the right side navigation menu')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    sign_in_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy'][normalize-space()='Sign in']")))
    sign_in_link.click()

@then('I should see the Sign In form')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    sign_in_form = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Sign into your Target account']")))
    assert sign_in_form is not None, "Sign In form not found"
    context.driver.quit()
