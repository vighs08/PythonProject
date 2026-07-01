from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://automationexercise.com")

assert "Automation Exercise" in driver.title

driver.find_element(By.LINK_TEXT, "Signup / Login").click()

assert driver.find_element(By.XPATH, "//h2[text()='Login to your account']").is_displayed()

driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("wronguser@gmail.com")
driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("Wrong@123")

driver.find_element(By.XPATH, "//button[text()='Login']").click()

time.sleep(5)

assert driver.find_element(By.XPATH, "//p[text()='Your email or password is incorrect!']").is_displayed()

driver.quit()