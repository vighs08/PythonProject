from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com")

print("Home page is visible successfully")

time.sleep(5)

test_case = driver.find_element(By.LINK_TEXT, "Test Cases")

driver.execute_script("arguments[0].scrollIntoView();", test_case)
time.sleep(2)

driver.execute_script("arguments[0].click();", test_case)

time.sleep(5)

print("Current URL:", driver.current_url)

if "test_cases" in driver.current_url:
    print("User is navigated to Test Cases page successfully")
else:
    print("Navigation failed")

driver.quit()