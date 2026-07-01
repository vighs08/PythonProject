from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to URL
    driver.get("https://automationexercise.com")
    time.sleep(3)

    print("Home page is visible successfully")

    # Scroll to bottom of page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Verify RECOMMENDED ITEMS
    recommended = driver.find_element(
        By.XPATH,
        "//*[contains(text(),'RECOMMENDED ITEMS')]"
    )

    if recommended.is_displayed():
        print("RECOMMENDED ITEMS are visible")

    # Click Add To Cart on a recommended product
    add_to_cart = driver.find_element(
        By.XPATH,
        "(//a[contains(@class,'add-to-cart')])[last()]"
    )

    driver.execute_script("arguments[0].click();", add_to_cart)
    time.sleep(3)

    # Click View Cart
    view_cart = driver.find_element(
        By.XPATH,
        "//u[contains(text(),'View Cart')]"
    )

    driver.execute_script("arguments[0].click();", view_cart)
    time.sleep(3)

    # Verify product displayed in cart
    products = driver.find_elements(
        By.XPATH,
        "//tr[contains(@id,'product')]"
    )

    if len(products) > 0:
        print("Product is displayed in cart page")
        print("TEST CASE PASSED")
    else:
        print("Product not found in cart")
        print("TEST CASE FAILED")

    input("Press Enter to close browser...")

except Exception as e:
    print("Error:", e)

finally:
    try:
        driver.close()
    except:
        pass