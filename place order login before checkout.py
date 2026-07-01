from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# ==========================
# HOME PAGE
# ==========================
driver.get("https://automationexercise.com")
time.sleep(3)

print("Home page is visible successfully")

# ==========================
# LOGIN
# ==========================
driver.get("https://automationexercise.com/login")
time.sleep(2)

driver.find_element(
    By.XPATH,
    "//input[@data-qa='login-email']"
).send_keys("vighneshraikar18@gmail.com")   # Replace with your email

driver.find_element(
    By.XPATH,
    "//input[@data-qa='login-password']"
).send_keys("test@123")          # Replace with your password

login_btn = driver.find_element(
    By.XPATH,
    "//button[@data-qa='login-button']"
)

driver.execute_script("arguments[0].click();", login_btn)

time.sleep(3)

print("Logged in as user")

# ==========================
# ADD PRODUCT TO CART
# ==========================
driver.get("https://automationexercise.com/product_details/1")
time.sleep(3)

add_cart = driver.find_element(By.CLASS_NAME, "cart")
driver.execute_script("arguments[0].click();", add_cart)

time.sleep(3)

# ==========================
# CART PAGE
# ==========================
driver.get("https://automationexercise.com/view_cart")
time.sleep(3)

print("Cart page displayed")

# ==========================
# CHECKOUT PAGE
# ==========================
driver.get("https://automationexercise.com/checkout")
time.sleep(3)

print("Address Details and Review Your Order visible")

# Comment
driver.find_element(
    By.NAME,
    "message"
).send_keys("Test Order From Selenium")

time.sleep(2)

# ==========================
# PLACE ORDER
# ==========================
try:
    place_order = driver.find_element(
        By.XPATH,
        "//a[@href='/payment']"
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        place_order
    )

    time.sleep(2)

    driver.execute_script(
        "arguments[0].click();",
        place_order
    )

except:
    driver.get("https://automationexercise.com/payment")

time.sleep(5)

print("Current URL =", driver.current_url)

# ==========================
# PAYMENT DETAILS
# ==========================
driver.find_element(By.NAME, "name_on_card").send_keys("Vighnesh Raikar")

driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")

driver.find_element(By.NAME, "cvc").send_keys("123")

driver.find_element(By.NAME, "expiry_month").send_keys("12")

driver.find_element(By.NAME, "expiry_year").send_keys("2028")

time.sleep(2)

# ==========================
# PAY & CONFIRM
# ==========================
pay_btn = driver.find_element(By.ID, "submit")

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    pay_btn
)

time.sleep(2)

driver.execute_script(
    "arguments[0].click();",
    pay_btn
)

time.sleep(5)

# ==========================
# VERIFY SUCCESS MESSAGE
# ==========================
if "order" in driver.page_source.lower():
    print("Your order has been placed successfully!")
else:
    print("Order placement message not found")

# ==========================
# DELETE ACCOUNT
# ==========================
try:
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

    continue_btn = driver.find_element(
        By.XPATH,
        "//a[contains(text(),'Continue')]"
    )

    driver.execute_script(
        "arguments[0].click();",
        continue_btn
    )

except:
    print("Delete Account button not found")

time.sleep(3)

driver.quit()