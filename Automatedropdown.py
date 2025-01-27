import time
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the dropdown demo page
    driver.get("https://demoqa.com/select-menu") 

    # Allow time for the page to load
    time.sleep(2)

    # Locate the dropdown menu using CSS Selector
    dropdown = driver.find_element(By.CSS_SELECTOR, "select#oldSelectMenu")

    # Select an option by index
    options = dropdown.find_elements(By.CSS_SELECTOR, "option")
    options[2].click()  

    time.sleep(1)

    # Select an option by value (e.g., value="4")
    option1 = dropdown.find_element(By.CSS_SELECTOR, "option[value='red']")
    option1.click()

    time.sleep(1)

    # Select an option by visible text (e.g., "Purple")
    for option in options:
        if option.text == "Purple":
            option.click()
        
            break
    time.sleep(1)

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser
    driver.quit()
