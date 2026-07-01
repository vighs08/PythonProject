from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to URL
driver.get("https://automationexercise.com")
time.sleep(3)

# Verify home page is visible
if "Automation Exercise" in driver.title:
    print("Home page is visible successfully")

# Scroll down to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# Verify SUBSCRIPTION is visible
subscription = driver.find_element(
    By.XPATH,
    "//h2[contains(text(),'Subscription')]"
)

if subscription.is_displayed():
    print("SUBSCRIPTION is visible")

# Scroll up to top without using arrow button
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(3)

# Verify page is scrolled up and text is visible
top_text = driver.find_element(
    By.XPATH,
    "//*[contains(text(),'Full-Fledged practice website for Automation Engineers')]"
)

if top_text.is_displayed():
    print("Page scrolled up successfully")
    print("Text is visible")

time.sleep(5)
driver.quit()