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
if "Automation Exercise" in driver.title:
    print("Home page is visible successfully")

# Open first product directly
driver.get("https://automationexercise.com/product_details/1")
time.sleep(2)

# Add product to cart
add_to_cart = driver.find_element(By.CLASS_NAME, "cart")
driver.execute_script("arguments[0].click();", add_to_cart)

time.sleep(3)

# Open Cart page
driver.get("https://automationexercise.com/view_cart")
time.sleep(3)

print("Cart page is displayed")

# Verify product exists
products = driver.find_elements(By.XPATH, "//tr[contains(@id,'product')]")

if len(products) > 0:
    print("Product added to cart")

# Click X button to remove product
delete_btn = driver.find_element(
    By.XPATH,
    "//a[@class='cart_quantity_delete']"
)

driver.execute_script("arguments[0].click();", delete_btn)

time.sleep(3)

# Verify product removed
products_after = driver.find_elements(
    By.XPATH,
    "//tr[contains(@id,'product')]"
)

if len(products_after) == 0:
    print("Product removed from cart successfully")
else:
    print("Product still exists in cart")

time.sleep(2)
driver.quit()