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
driver.find_element(
    By.XPATH,
    "//a[@href='/products']"
).click()

time.sleep(3)

# Verify Brands section
brands = driver.find_element(
    By.XPATH,
    "//h2[text()='Brands']"
)

if brands.is_displayed():
    print("Brands are visible on left sidebar")

# Click first brand (Polo)
brand1 = driver.find_element(
    By.XPATH,
    "//a[@href='/brand_products/Polo']"
)

driver.execute_script(
    "arguments[0].click();",
    brand1
)

time.sleep(3)

# Verify brand page
heading1 = driver.find_element(
    By.XPATH,
    "//h2[@class='title text-center']"
).text

print("Brand Page:", heading1)

if "BRAND" in heading1.upper():
    print("Brand products displayed successfully")

# Click another brand (H&M)
brand2 = driver.find_element(
    By.XPATH,
    "//a[@href='/brand_products/H&M']"
)

driver.execute_script(
    "arguments[0].click();",
    brand2
)

time.sleep(3)

# Verify second brand page
heading2 = driver.find_element(
    By.XPATH,
    "//h2[@class='title text-center']"
).text

print("Brand Page:", heading2)

if "BRAND" in heading2.upper():
    print("Second brand products displayed successfully")

time.sleep(3)
driver.quit()