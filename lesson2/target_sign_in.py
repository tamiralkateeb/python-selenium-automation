import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrom_options = Options()
chrom_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrom_options)

try:
    driver.get("https://www.target.com/")
    sign_in_button = driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']")
    sign_in_button.click()

    time.sleep(2)

    side_nav_sign_in = driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']")
    side_nav_sign_in.click()
    time.sleep(2)

    sign_in_text = driver.find_element(By.XPATH, "//span[normalize-space()='Sign into your Target account']")
    print("SignI into your target acounte i shown", sign_in_text)

    login_butoon = driver.find_element(By.XPATH, "//button[@id='login']")
    print("sign in button is shown", login_butoon)

finally:
    time.sleep(1)
    driver.quit()
