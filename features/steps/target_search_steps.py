# lesson4/features/steps/target_search_steps.py
from time import sleep

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I open the Target homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get('https://www.target.com')
    context.browser.maximize_window()


@when('I search for "{product}"')
def step_impl(context, product):
    search_box = context.browser.find_element(By.ID, 'search')
    search_box.send_keys(product)
    search_box.submit()


@then('I should see search results for {product}')
def step_impl(context, product):
    try:
        sleep(2)
        results = context.browser.find_element(By.XPATH, "//div[@data-test='resultsHeading']")
        results = results.text
        assert product.lower() in results.lower(), f"{product} not found in results"

        # if results:
        #     print(f"Number of product cards found: {len(results)}")
        #     for result in results:
        #         print(result.text)
        # else:
        #     print("No product cards found with the specified XPath.")

        # assert any(product.lower() in result.text.lower() for result in results), f"No search results for '{product}' found."
    finally:
        context.browser.quit()
