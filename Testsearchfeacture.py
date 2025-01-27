from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()

try:
    # Navigate to the Amazon homepage
    driver.get("https://www.amazon.com")

    # Wait for the page to load
    time.sleep(3)

    # Locate the search bar
    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")

    # Enter the search term and initiate the search
    search_term = "laptops"
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.RETURN)

    # Wait for the results page to load
    time.sleep(3)

    # Locate the product names in the search results
    product_titles = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")

    # Verify if the results contain the search term
    print("Search Results Verification:")
    for title in product_titles:
        product_text = title.text.lower()
        if search_term.lower() in product_text:
            print(f"Matched: {title.text}")
        else:
            print(f"Not Matched: {title.text}")

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser
    driver.quit()
