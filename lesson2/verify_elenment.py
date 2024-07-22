from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get(
    "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=7KT260D7P2AE773YY6MS&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

amazon_logo = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
print("Amazon logo", amazon_logo)

email_fields = driver.find_elements(By.ID, "ap_email")
print("Eamil ", email_fields)

continue_button = driver.find_element(By.XPATH, "//span[@id='continue']")
print("Continuing ", continue_button)

conditions_link = driver.find_element(By.XPATH, "//*[@id='legalTextRow']/a[1]")
print("Conditions ", conditions_link)

privacy_link = driver.find_element(By.XPATH, "//*[@id='legalTextRow']/a[2]")
print("Privacy ", privacy_link)

help_link = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
print("Help ", help_link)

shop_link = driver.find_element(By.XPATH, "//span[normalize-space()='Shop on Amazon Business']")
print("Shop ", shop_link)

create_account_link = driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")
print("Create Account ", create_account_link)
driver.close()
