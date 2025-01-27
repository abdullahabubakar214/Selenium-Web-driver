from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()

try:
    # Navigate to the hoverable elements page
    driver.get("https://demoqa.com/tool-tips")

    # Locate the element to hover over
    hover_element = driver.find_element(By.ID, "toolTipButton")

    # Perform hover action using ActionChains
    action = ActionChains(driver)
    action.move_to_element(hover_element).perform()

    # Wait to ensure the tooltip is displayed
    time.sleep(2)

    # Locate the tooltip element
    tooltip = driver.find_element(By.CSS_SELECTOR, ".tooltip-inner")

    # Verify the tooltip text
    expected_tooltip_text = "You hovered over the Button"
    actual_tooltip_text = tooltip.text

    if actual_tooltip_text == expected_tooltip_text:
        print("Tooltip verification successful!")
        print(f"Tooltip Text: {actual_tooltip_text}")
    else:
        print("Tooltip verification failed!")
        print(f"Expected: {expected_tooltip_text}, Found: {actual_tooltip_text}")

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser
    driver.quit()
