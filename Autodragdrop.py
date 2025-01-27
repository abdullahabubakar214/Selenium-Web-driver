from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()

try:
    # Navigate to the drag-and-drop page
    driver.get("https://demoqa.com/droppable")

    # Locate the source and target elements
    source_element = driver.find_element(By.ID, "draggable")
    target_element = driver.find_element(By.ID, "droppable")

    # Perform drag-and-drop action using ActionChains
    action = ActionChains(driver)
    action.drag_and_drop(source_element, target_element).perform()

    # Wait to observe the result
    time.sleep(2)

    # Verify if the drag-and-drop was successful
    target_text = target_element.text
    if "Dropped!" in target_text:
        print("Drag-and-drop successful!")
    else:
        print("Drag-and-drop failed!")
        print(f"Target text: {target_text}")

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser
    driver.quit()
