from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Home page
driver.get("https://automationexercise.com")
time.sleep(3)

print("Home page is visible successfully")

# Open first product directly
driver.get("https://automationexercise.com/product_details/1")
time.sleep(2)

# Add product to cart
driver.find_element(By.CLASS_NAME, "cart").click()
time.sleep(2)

# Open cart directly
driver.get("https://automationexercise.com/view_cart")
time.sleep(2)

print("Cart page is displayed")

# Proceed to checkout
checkout_btn = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'Proceed To Checkout')]"
)

driver.execute_script("arguments[0].click();", checkout_btn)
time.sleep(2)

# Register/Login
register_btn = driver.find_element(
    By.XPATH,
    "//u[contains(text(),'Register / Login')]"
)

driver.execute_script("arguments[0].click();", register_btn)
time.sleep(2)

# Signup
name = "Vighnesh"
email = f"vighnesh{int(time.time())}@gmail.com"

driver.find_element(By.NAME, "name").send_keys(name)

driver.find_element(
    By.XPATH,
    "//input[@data-qa='signup-email']"
).send_keys(email)

driver.find_element(
    By.XPATH,
    "//button[contains(text(),'Signup')]"
).click()

time.sleep(3)

# Account Information
driver.find_element(By.ID, "id_gender1").click()

driver.find_element(By.ID, "password").send_keys("Test@123")

driver.find_element(By.ID, "first_name").send_keys("Vighnesh")
driver.find_element(By.ID, "last_name").send_keys("Raikar")
driver.find_element(By.ID, "address1").send_keys("Bachhalli")
driver.find_element(By.ID, "country").send_keys("India")
driver.find_element(By.ID, "state").send_keys("Karnataka")
driver.find_element(By.ID, "city").send_keys("Mysore")
driver.find_element(By.ID, "zipcode").send_keys("570001")
driver.find_element(By.ID, "mobile_number").send_keys("9876543210")

driver.find_element(
    By.XPATH,
    "//button[contains(text(),'Create Account')]"
).click()

time.sleep(3)

print("ACCOUNT CREATED!")

# Continue
continue_btn = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'Continue')]"
)

driver.execute_script("arguments[0].click();", continue_btn)

time.sleep(3)

print("Logged in successfully")

# Open Cart directly
driver.get("https://automationexercise.com/view_cart")
time.sleep(2)

# Open Checkout directly
driver.get("https://automationexercise.com/checkout")
time.sleep(3)

print("Address Details and Review Your Order visible")

# Comment
driver.find_element(
    By.NAME,
    "message"
).send_keys("Please deliver quickly")

# Place Order
place_order = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'Place Order')]"
)

driver.execute_script("arguments[0].click();", place_order)

time.sleep(3)

# Payment Details
driver.find_element(
    By.NAME,
    "name_on_card"
).send_keys("Vighnesh Raikar")

driver.find_element(
    By.NAME,
    "card_number"
).send_keys("4111111111111111")

driver.find_element(
    By.NAME,
    "cvc"
).send_keys("123")

driver.find_element(
    By.NAME,
    "expiry_month"
).send_keys("12")

driver.find_element(
    By.NAME,
    "expiry_year"
).send_keys("2028")

time.sleep(2)

# Pay and Confirm Order
pay_button = driver.find_element(By.ID, "submit")

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    pay_button
)

time.sleep(2)

driver.execute_script(
    "arguments[0].click();",
    pay_button
)

time.sleep(5)

print("Your order has been placed successfully!")

# Delete Account
delete_btn = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'Delete Account')]"
)

driver.execute_script(
    "arguments[0].click();",
    delete_btn
)

time.sleep(3)

print("ACCOUNT DELETED!")

# Continue
continue_btn = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'Continue')]"
)

driver.execute_script(
    "arguments[0].click();",
    continue_btn
)

time.sleep(3)

driver.quit()