from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://automationexercise.com")
time.sleep(3)

print("Home page is visible successfully")

# Open product details page
driver.get("https://automationexercise.com/product_details/1")
time.sleep(3)

print("Product detail page is opened")

# Change quantity to 4
qty = driver.find_element(By.ID, "quantity")
qty.clear()
qty.send_keys("4")

time.sleep(1)

# Click Add to Cart
driver.find_element(By.CLASS_NAME, "cart").click()

time.sleep(2)

# Click View Cart
driver.find_element(
    By.XPATH,
    "//u[contains(text(),'View Cart')]"
).click()

time.sleep(3)

# Verify quantity
cart_qty = driver.find_element(
    By.XPATH,
    "//button[@class='disabled']"
).text

print("Quantity in cart:", cart_qty)

if cart_qty == "4":
    print("Product displayed in cart with exact quantity 4")
else:
    print("Quantity verification failed")

time.sleep(5)
driver.quit()