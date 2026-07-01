from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create driver
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://demoqa.com/checkbox")

# Wait for checkbox to be clickable
wait = WebDriverWait(driver, 10)
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='rct-checkbox']")))

# Click checkbox
checkbox.click()

# Verify (Note: span is not selectable → use class change instead)
if "rct-icon-check" in checkbox.get_attribute("innerHTML"):
    print("Checkbox selected successfully")
else:
    print("Checkbox selection failed")

# Unselect checkbox
checkbox.click()

# Verify unselect
if "rct-icon-check" not in checkbox.get_attribute("innerHTML"):
    print("Checkbox unselected successfully")
else:
    print("Checkbox unselection failed")

# Close browser
driver.quit()