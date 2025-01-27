import time
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore


driver = webdriver.Chrome()

try:

    driver.get("https://the-internet.herokuapp.com/iframe")


    time.sleep(2)

    # Switch to the iframe using its CSS selector
    iframe = driver.find_element(By.CSS_SELECTOR, "iframe#mce_0_ifr")
    driver.switch_to.frame(iframe)

    time.sleep(3)

    # Interact with the editor inside the iframe
    editor = driver.find_element(By.CSS_SELECTOR, "body#tinymce")
    # driver.execute_script("arguments[0].focus();", editor)  # Explicitly focus the editor
    editor.clear()
    editor.send_keys("Hello, this is a test message!") 

    time.sleep(3)

    # Switch back to the default content
    driver.switch_to.default_content()

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser
    driver.quit()
