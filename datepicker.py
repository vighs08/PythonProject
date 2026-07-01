from datetime import datetime,timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/datepicker/")
driver.maximize_window()
simple=driver.find_element(By.CSS_SELECTOR,"#post-2661 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p > iframe")
driver.switch_to.frame(simple)
date_picker=driver.find_element(By.ID,"datepicker")
date_picker.click()
current_date=datetime.now()
print(current_date)
next_date=current_date+timedelta(days=1)
print(next_date)
formatted_date=current_date.strftime("%m-%d-%Y")
print(formatted_date)
