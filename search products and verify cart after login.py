from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://automationexercise.com")
time.sleep(3)

# Click Products
products_btn = driver.find_element(
    By.XPATH,
    "//a[@href='/products']"
)
driver.execute_script("arguments[0].click();", products_btn)

time.sleep(3)

print("ALL PRODUCTS page opened")

# Search Product
driver.find_element(
    By.ID,
    "search_product"
).send_keys("Blue Top")

driver.find_element(
    By.ID,
    "submit_search"
).click()

time.sleep(3)

# Verify SEARCHED PRODUCTS
heading = driver.find_element(
    By.XPATH,
    "//h2[@class='title text-center']"
).text

if "SEARCHED PRODUCTS" in heading:
    print("SEARCHED PRODUCTS is visible")

# Verify products found
products = driver.find_elements(
    By.XPATH,
    "//div[@class='productinfo text-center']"
)

print("Products found:", len(products))

# Add first searched product to cart
add_buttons = driver.find_elements(
    By.XPATH,
    "//a[contains(@class,'add-to-cart')]"
)

driver.execute_script(
    "arguments[0].click();",
    add_buttons[0]
)

time.sleep(2)

# Continue Shopping
continue_btn = driver.find_element(
    By.XPATH,
    "//button[text()='Continue Shopping']"
)

driver.execute_script(
    "arguments[0].click();",
    continue_btn
)

time.sleep(2)

# Open Cart
driver.get("https://automationexercise.com/view_cart")
time.sleep(3)

print("Cart page displayed")

cart_products_before = driver.find_elements(
    By.XPATH,
    "//tr[contains(@id,'product')]"
)

print("Products in cart before login:", len(cart_products_before))

# Login
driver.get("https://automationexercise.com/login")
time.sleep(3)

driver.find_element(
    By.XPATH,
    "//input[@data-qa='login-email']"
).send_keys("vighneshraikar18@gmail.com")

driver.find_element(
    By.XPATH,
    "//input[@data-qa='login-password']"
).send_keys("test@123")

login_btn = driver.find_element(
    By.XPATH,
    "//button[@data-qa='login-button']"
)

driver.execute_script(
    "arguments[0].click();",
    login_btn
)

time.sleep(5)

print("Logged in successfully")

# Open Cart again
driver.get("https://automationexercise.com/view_cart")
time.sleep(3)

cart_products_after = driver.find_elements(
    By.XPATH,
    "//tr[contains(@id,'product')]"
)

print("Products in cart after login:", len(cart_products_after))

if len(cart_products_after) > 0:
    print("Products are visible in cart after login")
else:
    print("Products not found in cart after login")

time.sleep(3)
driver.quit()