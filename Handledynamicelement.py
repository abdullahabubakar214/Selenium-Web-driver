from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:
    # Navigate to a page with dynamically loaded elements
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    # Click the 'Start' button to load dynamic content
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    # Wait for the dynamic element to become visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # Extract text from the dynamically loaded element
    dynamic_text = driver.find_element(By.CSS_SELECTOR, "#finish h4").text
    print(f"Dynamic Text: {dynamic_text}")

except Exception as e:
    print("Error:", e)

finally:
    
    driver.quit()
