import time
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Google homepage
driver.get(" https://the-internet.herokuapp.com/login")

# Allow time for the page to load
time.sleep(3)

try:

    username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    username.send_keys("Abdullah Abu Bakar")

    username = driver.find_element(By.CSS_SELECTOR, "input#password")
    username.send_keys("123 Bakar\n")
    
    # Wait for 10 seconds to keep the browser open
    time.sleep(1000)
    
except Exception as e:
    print("Error:", e)

# Close the browser
driver.quit()