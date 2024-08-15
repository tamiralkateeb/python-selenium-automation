from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrom_options = Options()
chrom_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrom_options)

try:
    driver.get("https://www.target.com/")

    # Wait for the Sign In button to be clickable and then click it
    wait = WebDriverWait(driver, 10)
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Account, sign in']")))
    sign_in_button.click()

    # Wait for the Sign In link in the side navigation menu to be clickable and then click it
    side_nav_sign_in = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-test='accountNav-signIn']")))
    side_nav_sign_in.click()

    # Wait for the Sign In form text to be visible
    sign_in_text = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Sign into your Target account']")))
    print("Sign in form is shown:", sign_in_text.is_displayed())

    # Wait for the Login button to be visible
    login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='login']")))
    print("Sign in button is shown:", login_button.is_displayed())

finally:
    driver.quit()
