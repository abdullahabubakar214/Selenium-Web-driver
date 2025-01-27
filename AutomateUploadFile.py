import time
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore

# Initialize WebDriver
driver = webdriver.Chrome()

try:

    driver.get("https://the-internet.herokuapp.com/upload")

    choose_file = driver.find_element(By.CSS_SELECTOR, "input#file-upload")
    file_path = "F:\web_driver.txt"
    choose_file.send_keys(file_path)

    time.sleep(2)

    upload_file = driver.find_element(By.CSS_SELECTOR, "input#file-submit")
    upload_file.click()

    time.sleep(2)

    uploaded_file = driver.find_element(By.CSS_SELECTOR, "div#uploaded-files")
    uploaded_file_name = uploaded_file.text

    # print("Uploaded file:",uploaded_file_name)
    
    

    time.sleep(20000)

except Exception as e:
    print("Error:", e)

finally:
 
    driver.quit()
