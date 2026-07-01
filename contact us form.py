from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open website
driver.get("https://automationexercise.com")
driver.maximize_window()

# Verify Home Page
print("Home Page Title:", driver.title)

# Click Contact Us
driver.find_element(By.LINK_TEXT, "Contact us").click()
time.sleep(2)

# Fill Contact Form
driver.find_element(By.NAME, "name").send_keys("Vighnesh Raikar")
driver.find_element(By.NAME, "email").send_keys("vighnesh@gmail.com")
driver.find_element(By.NAME, "subject").send_keys("Selenium Test")
driver.find_element(By.NAME, "message").send_keys(
    "This is a test message submitted using Selenium."
)

# Upload File
file_path = r"C:\Users\vighnesh raikar\OneDrive\Documents\BCA\TY\SEM 5\Computer Animation\OpenToonz stuff\profiles\project_folders.txt"
driver.find_element(By.NAME, "upload_file").send_keys(file_path)

# Click Submit
driver.find_element(By.NAME, "submit").click()

# Accept Alert Popup
driver.switch_to.alert.accept()
time.sleep(2)

# Verify Success Message
success_msg = driver.find_element(By.CLASS_NAME, "status").text
print("Success Message:", success_msg)

# Click Home Button
driver.find_element(By.XPATH, "//a[contains(text(),'Home')]").click()
time.sleep(2)

# Verify Home Page Again
print("Returned to Home Page Successfully")
print("Current URL:", driver.current_url)

# Close Browser
time.sleep(3)
driver.quit()