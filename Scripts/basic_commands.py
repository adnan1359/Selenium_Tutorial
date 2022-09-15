from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://chrome.google.com/webstore/category/extensions"

driver = webdriver.Chrome()
driver.get(URL)

text = driver.find_element(By.CLASS_NAME, 'a-d-l-L').click()

time.sleep(10)

# Closes currently focussed browser
# driver.close()


# Closes all open browsers
driver.quit()