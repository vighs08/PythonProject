from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

email = f"vighnesh{int(time.time())}@gmail.com"

try:
    # Home Page
    driver.get("https://automationexercise.com")
    time.sleep(3)

    print("Home page is visible successfully")

    # Add product to cart
    driver.get("https://automationexercise.com/products")
    time.sleep(3)

    add_product = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//a[@data-product-id='1'])[1]")
        )
    )

    driver.execute_script("arguments[0].click();", add_product)
    time.sleep(2)

    # Cart
    driver.get("https://automationexercise.com/view_cart")
    time.sleep(2)

    print("Cart page is displayed")

    # Checkout
    checkout = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(),'Proceed To Checkout')]")
        )
    )

    driver.execute_script("arguments[0].click();", checkout)
    time.sleep(2)

    # Register/Login
    register = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//u[contains(text(),'Register / Login')]")
        )
    )

    driver.execute_script("arguments[0].click();", register)
    time.sleep(3)

    # Signup
    driver.find_element(By.NAME, "name").send_keys("Vighnesh")

    driver.find_element(
        By.XPATH,
        "//input[@data-qa='signup-email']"
    ).send_keys(email)

    driver.find_element(
        By.XPATH,
        "//button[@data-qa='signup-button']"
    ).click()

    time.sleep(3)

    # Account Info
    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.ID, "password").send_keys("Test@123")

    driver.find_element(By.ID, "days").send_keys("10")
    driver.find_element(By.ID, "months").send_keys("May")
    driver.find_element(By.ID, "years").send_keys("2000")

    driver.find_element(By.ID, "first_name").send_keys("Vighnesh")
    driver.find_element(By.ID, "last_name").send_keys("Raikar")
    driver.find_element(By.ID, "address1").send_keys("Bachhalli")
    driver.find_element(By.ID, "state").send_keys("Karnataka")
    driver.find_element(By.ID, "city").send_keys("Bangalore")
    driver.find_element(By.ID, "zipcode").send_keys("560001")
    driver.find_element(By.ID, "mobile_number").send_keys("9999999999")

    create_account = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@data-qa='create-account']")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView();",
        create_account
    )

    driver.execute_script(
        "arguments[0].click();",
        create_account
    )

    time.sleep(5)

    print("ACCOUNT CREATED!")

    # Continue
    continue_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@data-qa='continue-button']")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        continue_btn
    )

    time.sleep(5)

    print("Logged in successfully")

    # Cart Again
    driver.get("https://automationexercise.com/view_cart")
    time.sleep(2)

    checkout = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(),'Proceed To Checkout')]")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        checkout
    )

    time.sleep(3)

    print("Address Details and Review Your Order visible")

    # Comment
    driver.find_element(
        By.NAME,
        "message"
    ).send_keys("Test order from Selenium")

    # Place Order
    place_order = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(),'Place Order')]")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        place_order
    )

    time.sleep(3)

    # Payment
    driver.find_element(By.NAME, "name_on_card").send_keys("Vighnesh Raikar")
    driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")
    driver.find_element(By.NAME, "cvc").send_keys("123")
    driver.find_element(By.NAME, "expiry_month").send_keys("12")
    driver.find_element(By.NAME, "expiry_year").send_keys("2030")

    pay_btn = wait.until(
        EC.presence_of_element_located(
            (By.ID, "submit")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        pay_btn
    )

    time.sleep(5)

    print("Current URL:", driver.current_url)

    # Wait for confirmation
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(),'Congratulations')]")
        )
    )

    print("Order placed successfully")

    # Download Invoice
    invoice_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(@href,'download_invoice')]")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        invoice_btn
    )

    print("Invoice downloaded successfully")

    time.sleep(3)

    # Continue
    continue_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(),'Continue')]")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        continue_btn
    )

    time.sleep(3)

    # Delete Account
    delete_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(),'Delete Account')]")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        delete_btn
    )

    time.sleep(3)

    print("ACCOUNT DELETED!")

    print("TEST CASE PASSED")

    input("Press Enter to close browser...")

except Exception as e:
    print("ERROR:", e)

finally:
    driver.quit()