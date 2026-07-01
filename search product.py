from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Open home page
driver.get("https://automationexercise.com")
time.sleep(3)

print("Home page is visible successfully")

# Open Products page directly
driver.get("https://automationexercise.com/products")
time.sleep(3)

print("User is navigated to ALL PRODUCTS page successfully")

# Search product
driver.find_element(By.ID, "search_product").send_keys("Blue Top")
driver.find_element(By.ID, "submit_search").click()

time.sleep(3)

# Verify SEARCHED PRODUCTS
heading = driver.find_element(
    By.XPATH,
    "//h2[contains(text(),'Searched Products')]"
).text

print(heading)

# Verify products displayed
products = driver.find_elements(By.CLASS_NAME, "product-image-wrapper")

if len(products) > 0:
    print("All the products related to search are visible")
else:
    print("No products found")

time.sleep(5)
driver.quit()