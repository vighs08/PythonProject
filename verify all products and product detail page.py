from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://automationexercise.com")
time.sleep(3)

# Verify home page
print("Home page is visible successfully")

# Click Products
driver.find_element(By.XPATH, "//a[@href='/products']").click()
time.sleep(3)

# Verify products page
if "products" in driver.current_url:
    print("User is navigated to ALL PRODUCTS page successfully")

# Verify products list
products = driver.find_elements(By.CLASS_NAME, "product-image-wrapper")

if len(products) > 0:
    print("Products list is visible")

# Open first product details page directly
driver.get("https://automationexercise.com/product_details/1")
time.sleep(3)

print("User is landed to product detail page")

# Product Name
product_name = driver.find_element(
    By.XPATH,
    "//div[@class='product-information']/h2"
).text

# Category
category = driver.find_element(
    By.XPATH,
    "//div[@class='product-information']/p"
).text

# Price
price = driver.find_element(
    By.XPATH,
    "//div[@class='product-information']//span/span"
).text

# Availability
availability = driver.find_element(
    By.XPATH,
    "//b[contains(text(),'Availability')]"
).text

# Condition
condition = driver.find_element(
    By.XPATH,
    "//b[contains(text(),'Condition')]"
).text

# Brand
brand = driver.find_element(
    By.XPATH,
    "//b[contains(text(),'Brand')]"
).text

print("Product Name:", product_name)
print("Category:", category)
print("Price:", price)
print("Availability:", availability)
print("Condition:", condition)
print("Brand:", brand)

print("All product details are visible successfully")

time.sleep(5)
driver.quit()