from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to URL
driver.get("https://automationexercise.com")
time.sleep(3)

# Verify home page
print("Home page is visible successfully")

# Scroll down to footer
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Verify SUBSCRIPTION text
subscription = driver.find_element(By.XPATH, "//h2[text()='Subscription']").text

if "SUBSCRIPTION" in subscription.upper():
    print("SUBSCRIPTION is visible")

# Enter email address
driver.find_element(By.ID, "susbscribe_email").send_keys("vighnesh@gmail.com")

# Click arrow button
driver.find_element(By.ID, "subscribe").click()

time.sleep(3)

# Verify success message
message = driver.find_element(By.XPATH, "//div[@class='alert-success alert']").text

if "successfully subscribed" in message.lower():
    print("You have been successfully subscribed!")

time.sleep(5)
driver.quit()