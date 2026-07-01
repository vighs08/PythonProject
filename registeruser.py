from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random

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

# verify signup page
assert driver.find_element(
    By.XPATH,
    "//h2[text()='New User Signup!']"
).is_displayed()

print("Signup page is visible")

# create random email
email = f"user{random.randint(1000,9999)}@gmail.com"

# enter name
driver.find_element(By.NAME, "name").send_keys("Test User")

# enter email
driver.find_element(
    By.XPATH,
    "//input[@data-qa='signup-email']"
).send_keys(email)

# click signup button
driver.find_element(
    By.XPATH,
    "//button[text()='Signup']"
).click()

time.sleep(3)

# verify enter account information
assert driver.find_element(
    By.XPATH,
    "//b[text()='Enter Account Information']"
).is_displayed()

print("Enter Account Information is visible")

# select title
driver.find_element(By.ID, "id_gender1").click()

# enter password
driver.find_element(By.ID, "password").send_keys("Test@123")

# select date of birth
Select(driver.find_element(By.ID, "days")).select_by_visible_text("8")

Select(driver.find_element(By.ID, "months")).select_by_visible_text("February")

Select(driver.find_element(By.ID, "years")).select_by_visible_text("2004")

# click checkboxes
driver.find_element(By.ID, "newsletter").click()
driver.find_element(By.ID, "optin").click()

# fill address details
driver.find_element(By.ID, "first_name").send_keys("Vighnesh")
driver.find_element(By.ID, "last_name").send_keys("Raikar")
driver.find_element(By.ID, "company").send_keys("ABC Pvt Ltd")
driver.find_element(By.ID, "address1").send_keys("Street 1")
driver.find_element(By.ID, "address2").send_keys("Area")

# select country
Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")

# fill remaining details
driver.find_element(By.ID, "state").send_keys("Goa")
driver.find_element(By.ID, "city").send_keys("Margao")
driver.find_element(By.ID, "zipcode").send_keys("403602")
driver.find_element(By.ID, "mobile_number").send_keys("7757919534")

# click create account
driver.find_element(
    By.XPATH,
    "//button[text()='Create Account']"
).click()

time.sleep(3)

# verify account created
assert driver.find_element(
    By.XPATH,
    "//b[text()='Account Created!']"
).is_displayed()

print("Account created successfully")

# click continue
driver.find_element(By.XPATH, "//a[text()='Continue']").click()

time.sleep(5)

# verify logged in
assert driver.find_element(
    By.XPATH,
    "//a[contains(text(),'Logged in as')]"
).is_displayed()

print("User logged in successfully")

# delete account
delete_btn = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'Delete Account')]"
)

driver.execute_script(
    "arguments[0].scrollIntoView();",
    delete_btn
)

time.sleep(2)

delete_btn.click()

time.sleep(3)

# verify account deleted
assert driver.find_element(
    By.XPATH,
    "//b[text()='Account Deleted!']"
).is_displayed()

print("Account deleted successfully")

# click continue button
driver.find_element(By.XPATH, "//a[text()='Continue']").click()

time.sleep(2)

# close browser
driver.quit()