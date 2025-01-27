import time
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the table demo page
    driver.get("https://www.seleniumeasy.com/test/table-sort-search-demo.html")

    # Allow time for the page to load
    time.sleep(2)

    # Locate the table body using a CSS selector
    table_body = driver.find_element(By.CSS_SELECTOR, "table#example tbody")

    # Get all rows in the table body
    rows = table_body.find_elements(By.CSS_SELECTOR, "tr")

    # Loop through rows and extract data
    extracted_data = []
    for row in rows:
        # Get all cells in the current row
        cells = row.find_elements(By.CSS_SELECTOR, "td")
        row_data = [cell.text for cell in cells]
        extracted_data.append(row_data)

    # Print the extracted data
    for row in extracted_data:
        print(row)

    # Verify the presence of specific data (e.g., check if "Airi Satou" is in the table)
    specific_data = "Airi Satou"
    found = any(specific_data in row for row in extracted_data)
    if found:
        print(f"Data '{specific_data}' found in the table.")
    else:
        print(f"Data '{specific_data}' not found in the table.")

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser
    driver.quit()
