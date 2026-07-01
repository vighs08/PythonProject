import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/iframe")

ele = driver.find_element(By.ID, "mce_0_ifr")

driver.switch_to.frame("mce_0_ifr")

txtarea = driver.find_element(By.ID, "tinymce")

driver.switch_to.default_content()

time.sleep(2)

click_ele = driver.find_element(By.CSS_SELECTOR, "#page-footer > div > div > a").click()

time.sleep(2)