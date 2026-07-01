from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://automationexercise.com")
time.sleep(3)

# Click Products button
products_btn = driver.find_element(
    By.XPATH,
    "//a[@href='/products']"
)

driver.execute_script(
    "arguments[0].click();",
    products_btn
)

time.sleep(3)

print("ALL PRODUCTS page opened successfully")

# Open first product directly
driver.get("https://automationexercise.com/product_details/1")
time.sleep(3)

print("Product detail page opened")

# Verify Write Your Review
review_text = driver.find_element(
    By.XPATH,
    "//a[text()='Write Your Review']"
)

if review_text.is_displayed():
    print("Write Your Review is visible")

# Enter Name
driver.find_element(
    By.ID,
    "name"
).send_keys("Vighnesh Raikar")

# Enter Email
driver.find_element(
    By.ID,
    "email"
).send_keys("vighnesh@gmail.com")

# Enter Review
driver.find_element(
    By.ID,
    "review"
).send_keys(
    "This is a very good product. Quality is excellent."
)

time.sleep(2)

# Click Submit
submit_btn = driver.find_element(
    By.ID,
    "button-review"
)

driver.execute_script(
    "arguments[0].click();",
    submit_btn
)

time.sleep(3)

# Verify Success Message
success_msg = driver.find_element(
    By.XPATH,
    "//span[contains(text(),'Thank you for your review.')]"
)

if success_msg.is_displayed():
    print("Thank you for your review. - Message displayed")

time.sleep(3)

driver.quit()