from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")
top= driver.find_element(By.NAME,"frame-top")
driver.switch_to.frame("frame-top")
left=driver.find_element(By.NAME,"frame-left")
middle=driver.find_element(By.NAME,"frame-middle")
driver.switch_to.default_content()
time.sleep(3)
