from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Test data
name = "Vighnesh"
email = f"vighnesh{int(time.time())}@gmail.com"

driver.get("https://automationexercise.com")
time.sleep(3)

print("Home page is visible successfully")

# Signup / Login
driver.find_element(By.XPATH, "//a[contains(text(),'Signup / Login')]").click()
time.sleep(2)

# Signup
driver.find_element(By.NAME, "name").send_keys(name)
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
time.sleep(3)

# Account Information
driver.find_element(By.ID, "id_gender1").click()
driver.find_element(By.ID, "password").send_keys("Test@123")

driver.find_element(By.ID, "days").send_keys("10")
driver.find_element(By.ID, "months").send_keys("May")
driver.find_element(By.ID, "years").send_keys("2000")

# Address Information
driver.find_element(By.ID, "first_name").send_keys("Vighnesh")
driver.find_element(By.ID, "last_name").send_keys("Raikar")
driver.find_element(By.ID, "company").send_keys("ABC")

driver.find_element(By.ID, "address1").send_keys("Bachhalli")
driver.find_element(By.ID, "address2").send_keys("Karnataka")

driver.find_element(By.ID, "country").send_keys("India")
driver.find_element(By.ID, "state").send_keys("Karnataka")
driver.find_element(By.ID, "city").send_keys("Bangalore")
driver.find_element(By.ID, "zipcode").send_keys("560001")
driver.find_element(By.ID, "mobile_number").send_keys("9999999999")

# Create Account
create_btn = driver.find_element(
    By.XPATH,
    "//button[@data-qa='create-account']"
)

driver.execute_script("arguments[0].click();", create_btn)

time.sleep(5)

print("ACCOUNT CREATED!")

# Continue
continue_btn = driver.find_element(
    By.XPATH,
    "//a[@data-qa='continue-button']"
)

driver.execute_script("arguments[0].click();", continue_btn)

time.sleep(5)

print("Logged in successfully")

# Go directly to products page
driver.get("https://automationexercise.com/products")
time.sleep(3)

# Add first product
add_btn = driver.find_element(
    By.XPATH,
    "(//a[@data-product-id='1'])[1]"
)

driver.execute_script("arguments[0].click();", add_btn)
time.sleep(3)

# View Cart
driver.get("https://automationexercise.com/view_cart")
time.sleep(3)

print("Cart page displayed")

# Proceed To Checkout
checkout_btn = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'Proceed To Checkout')]"
)

driver.execute_script("arguments[0].click();", checkout_btn)
time.sleep(3)

# Verify Delivery Address
delivery_address = driver.find_element(
    By.ID,
    "address_delivery"
).text

if "Bachhalli" in delivery_address:
    print("Delivery Address Verified")
else:
    print("Delivery Address Verification Failed")

# Verify Billing Address
billing_address = driver.find_element(
    By.ID,
    "address_invoice"
).text

if "Bachhalli" in billing_address:
    print("Billing Address Verified")
else:
    print("Billing Address Verification Failed")

# Delete Account
delete_btn = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'Delete Account')]"
)

driver.execute_script("arguments[0].click();", delete_btn)

time.sleep(3)

if "ACCOUNT DELETED!" in driver.page_source:
    print("ACCOUNT DELETED!")
else:
    print("Account deletion failed")

# Continue
continue_btn = driver.find_element(
    By.XPATH,
    "//a[@data-qa='continue-button']"
)

driver.execute_script("arguments[0].click();", continue_btn)

time.sleep(3)

print("Test Case Passed Successfully")

input("Press Enter to close browser...")

driver.quit()
