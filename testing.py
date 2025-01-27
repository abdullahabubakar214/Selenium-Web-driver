from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver for Chrome
driver = webdriver.Chrome(executable_path='https://developer.chrome.com/docs/chromedriver')

try:
    # Open Google
    driver.get("https://www.google.com")

    # Get and print the browser name
    browser_name = driver.capabilities['browserName']
    print(f"Browser name: {browser_name}")

    # Find the Google search input box and write "White Board"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("White Board")
    search_box.send_keys(Keys.RETURN)

finally:
    # Close the browser after a short delay 
    driver.quit()
