from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (e.g., ChromeDriver)
driver = webdriver.Chrome()

try:
    # Navigate to the e-commerce website (replace with a valid URL)
    driver.get("https://www.amazon.com/s?k=laptops")  # Example: Amazon search results for "laptops"

    # Wait for the page to load completely
    time.sleep(3)

    # Locate the product elements (replace selectors with those of the target website)
    product_names = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal")
    product_prices = driver.find_elements(By.CSS_SELECTOR, "span.a-price-whole")

    # Extract and print product details
    print("Scraped Product Details:")
    for name, price in zip(product_names, product_prices):
        print(f"Product: {name.text}, Price: ${price.text}")

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser
    driver.quit()
