from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.HomePage import HomePage
from page_objects.SignInPage import SignInPage

@given('I open the Target website for sign in')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get("https://www.target.com/")
    context.driver.maximize_window()
    context.home_page = HomePage(context.driver)

@when('I click on the Sign In button')
def step_impl(context):
    context.home_page.click_sign_in()
    context.sign_in_page = SignInPage(context.driver)

@when('I click on the Sign In link from the right side navigation menu')
def step_impl(context):
    context.sign_in_page.click_side_nav_sign_in()

@then('I should see the Sign In form')
def step_impl(context):
    assert context.sign_in_page.is_sign_in_form_visible(), "Sign In form not found"
    context.driver.quit()
