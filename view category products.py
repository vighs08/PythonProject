from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://automationexercise.com")
time.sleep(3)

# Verify Categories section
categories = driver.find_element(By.XPATH, "//h2[text()='Category']")
if categories.is_displayed():
    print("Categories are visible on left sidebar")

# Click Women category
women_category = driver.find_element(
    By.XPATH,
    "//a[@href='#Women']"
)

driver.execute_script("arguments[0].click();", women_category)
time.sleep(2)

# Click Dress sub-category
dress = driver.find_element(
    By.XPATH,
    "//a[@href='/category_products/1']"
)

driver.execute_script("arguments[0].click();", dress)
time.sleep(3)

# Verify Women category page
heading = driver.find_element(
    By.XPATH,
    "//h2[@class='title text-center']"
).text

print("Category Page:", heading)

if "WOMEN" in heading.upper():
    print("Women category page displayed successfully")

# Click Men category
men_category = driver.find_element(
    By.XPATH,
    "//a[@href='#Men']"
)

driver.execute_script("arguments[0].click();", men_category)
time.sleep(2)

# Click Tshirts sub-category
tshirts = driver.find_element(
    By.XPATH,
    "//a[@href='/category_products/3']"
)

driver.execute_script("arguments[0].click();", tshirts)
time.sleep(3)

# Verify Men category page
heading2 = driver.find_element(
    By.XPATH,
    "//h2[@class='title text-center']"
).text

print("Category Page:", heading2)

if "MEN" in heading2.upper():
    print("Men category page displayed successfully")

time.sleep(3)
driver.quit()