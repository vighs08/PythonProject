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

# Open Products page directly
driver.get("https://automationexercise.com/products")
time.sleep(3)

# Add first product
add_product1 = driver.find_element(
    By.XPATH,
    "(//a[@data-product-id='1'])[1]"
)

driver.execute_script("arguments[0].click();", add_product1)

time.sleep(2)

# Continue Shopping
driver.find_element(
    By.XPATH,
    "//button[contains(text(),'Continue Shopping')]"
).click()

time.sleep(2)

# Add second product
add_product2 = driver.find_element(
    By.XPATH,
    "(//a[@data-product-id='2'])[1]"
)

driver.execute_script("arguments[0].click();", add_product2)

time.sleep(2)

# View Cart
driver.find_element(
    By.XPATH,
    "//u[contains(text(),'View Cart')]"
).click()

time.sleep(3)

# Verify products added
products = driver.find_elements(
    By.XPATH,
    "//tr[contains(@id,'product')]"
)

print("Number of products in cart:", len(products))

if len(products) == 2:
    print("Both products are added to cart successfully")

# Product 1 details
price1 = driver.find_element(
    By.XPATH,
    "(//td[@class='cart_price'])[1]"
).text

qty1 = driver.find_element(
    By.XPATH,
    "(//button[@class='disabled'])[1]"
).text

total1 = driver.find_element(
    By.XPATH,
    "(//p[@class='cart_total_price'])[1]"
).text

# Product 2 details
price2 = driver.find_element(
    By.XPATH,
    "(//td[@class='cart_price'])[2]"
).text

qty2 = driver.find_element(
    By.XPATH,
    "(//button[@class='disabled'])[2]"
).text

total2 = driver.find_element(
    By.XPATH,
    "(//p[@class='cart_total_price'])[2]"
).text

print("\nProduct 1")
print("Price:", price1)
print("Quantity:", qty1)
print("Total:", total1)

print("\nProduct 2")
print("Price:", price2)
print("Quantity:", qty2)
print("Total:", total2)

time.sleep(5)
driver.quit()