from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_target_color_selection():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://www.target.com/p/A-91511634")
        wait = WebDriverWait(driver, 20)

        try:
            color_section = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='above-the-fold-information'][contains(.,'color')]")))

            color_options = color_section.find_elements(By.XPATH, ".//li[contains(@data-test, 'swatch')]")

            for color in color_options:
                color.click()

                selected_color = wait.until(EC.visibility_of_element_located((By.XPATH, ".//li[contains(@data-test, 'swatch') and contains(@class, 'selected')]")))

                color_name = color.get_attribute("aria-label")
                print(f"Selected color: {color_name}")

                assert color_name in selected_color.get_attribute("aria-label"), f"Expected {color_name} to be selected, but got {selected_color.get_attribute('aria-label')}"

        except TimeoutException:
            print("The color swatches were not found within the given time.")

    finally:
        driver.quit()
