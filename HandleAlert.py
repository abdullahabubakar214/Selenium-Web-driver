import time
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.alert import Alert # type: ignore

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the JavaScript Alerts page
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    
    # Allow time for the page to load
    time.sleep(2)

    # Locate and click the button to trigger a simple alert
    alert_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    alert_button.click()
    
    # Switch to the alert
    alert = Alert(driver)
    
    # Extract the alert text
    alert_text = alert.text

 
    alert.accept()

    time.sleep(20000)

    # Trigger and dismiss a confirmation alert
    confirm_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    confirm_button.click()

    alert = Alert(driver)
    
    alert.dismiss()  # Dismiss the alert (click "Cancel")
    
    time.sleep(20000)

    # Trigger and interact with a prompt alert
    prompt_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
    prompt_button.click()

    alert = Alert(driver)
    
    alert.send_keys("Hello from Selenium!")  
    alert.accept()  

    time.sleep(20000)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
