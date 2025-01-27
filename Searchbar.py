import time
from selenium import webdriver 
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(3)
try:
    search_bar = driver.find_element(By.CSS_SELECTOR, "textarea[name='q']")
    # search_bar = driver.find_element(By.CSS_SELECTOR, "textarea.gLFyf")

    search_bar.send_keys("Any thing you want to search you can type")
    time.sleep(10)
    search_bar.click() 
    print("Abdullah Abu bakar, SP21-BSE-102")
    time.sleep(10)
    
except Exception as e:
    print("Error:", e)
driver.quit()