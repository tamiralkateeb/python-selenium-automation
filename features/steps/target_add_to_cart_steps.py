from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I open the Target website')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get("https://www.target.com/")
    context.driver.maximize_window()


@when('I search for a product')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    search_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))
    search_box.send_keys("mug root beer")
    search_button = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    search_button.click()


@when('I add the first product to the cart')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    first_product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div > section:nth-child(2) > div:nth-child(1) > div:nth-child(2)")))
    first_product.click()

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(3) > main:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > button:nth-child(2)")))
    add_to_cart_button.click()


@then('I should see the product in the cart')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='sc-9306beff-0 sc-c9f17d5d-0 dfqbQr jFvIkK']")))
    cart_icon.click()

    # Verify the cart is not empty by checking for cart items or total price
    cart_item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-c8b6049-1.cEZYWL")))
    assert cart_item.text == "1", f"Expected 1 item in the cart, but found {cart_item.text}"

    context.driver.quit()
