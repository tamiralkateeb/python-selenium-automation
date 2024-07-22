from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

@given('I open the Target website')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get("https://www.target.com/")
    context.driver.maximize_window()

@when('I click on the Cart icon')
def step_impl(context):
    cart_icon = context.driver.find_element(By.XPATH, "//a[@aria-label='cart 0 items']")
    cart_icon.click()
    time.sleep(2)

@then('I should see the message "Your cart is empty"')
def step_impl(context):
    empty_cart_message = context.driver.find_element(By.XPATH, "//h1[normalize-space()='Your cart is empty']")
    assert empty_cart_message is not None, "Empty cart message not found"
    context.driver.quit()