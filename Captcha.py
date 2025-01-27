from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()

try:
    # Navigate to a page with CAPTCHA (replace with a valid URL)
    driver.get("https://www.google.com/recaptcha/api2/demo")

    # Wait for the CAPTCHA to load
    time.sleep(5)

    # Locate CAPTCHA frame (if applicable)
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")
    driver.switch_to.frame(iframe)

    print("CAPTCHA detected. Please solve it manually...")
    
    # Pause for manual CAPTCHA solving
    while True:
        user_input = input("Type 'done' once you solve the CAPTCHA: ").strip().lower()
        if user_input == "done":
            break

    # Switch back to the default content
    driver.switch_to.default_content()

    # Resume automation (e.g., submit the form)
    submit_button = driver.find_element(By.ID, "recaptcha-demo-submit")
    submit_button.click()

    # Wait for a response or the next page to load
    time.sleep(5)

    print("CAPTCHA solved manually. Automation resumed.")

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser
    driver.quit()
