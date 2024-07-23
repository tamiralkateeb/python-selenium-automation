from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=69XZ0CY4EBMPW2WAVY3B&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    name_input = driver.find_element(By.XPATH, "//input[@id='ap_customer_name']")
    print("your name " , name_input)

    email_input = driver.find_element(By.XPATH, "//input[@id='ap_email']")
    print("your email " , email_input)


    password_input = driver.find_element(By.XPATH, "//input[@id='ap_password']")
    print("your password " , password_input)

    reenter_password_inpute = driver.find_element(By.XPATH, "//input[@id='ap_password_check']")
    print("your reenter password " , reenter_password_inpute)

    continue_account_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    print("your continue account " , continue_account_button)

finally:

    driver.quit()