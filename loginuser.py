from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# launch browser
driver = webdriver.Chrome()

# maximize browser
driver.maximize_window()

# open website
driver.get("http://automationexercise.com")

time.sleep(2)

# verify home page
assert "Automation Exercise" in driver.title
print("Home page is visible")

# click signup/login
driver.find_element(By.LINK_TEXT, "Signup / Login").click()

time.sleep(2)

# verify login page
assert driver.find_element(
    By.XPATH,
    "//h2[text()='Login to your account']"
).is_displayed()

print("Login page is visible")

# enter email
driver.find_element(
    By.XPATH,
    "//input[@data-qa='login-email']"
).send_keys("vighneshraikar18@gmail.com")

# enter password
driver.find_element(
    By.XPATH,
    "//input[@data-qa='login-password']"
).send_keys("test@123")

# click login button
driver.find_element(
    By.XPATH,
    "//button[text()='Login']"
).click()

time.sleep(5)

# verify logged in
assert driver.find_element(
    By.XPATH,
    "//a[contains(text(),'Logged in as')]"
).is_displayed()

print("User logged in successfully")

# find delete account button
delete_btn = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'Delete Account')]"
)

# scroll to delete button
driver.execute_script(
    "arguments[0].scrollIntoView();",
    delete_btn
)

time.sleep(2)

# click delete account
delete_btn.click()

time.sleep(5)

# verify account deleted
assert driver.find_element(
    By.XPATH,
    "//b[text()='Account Deleted!']"
).is_displayed()

print("Account deleted successfully")

# close browser
driver.quit()