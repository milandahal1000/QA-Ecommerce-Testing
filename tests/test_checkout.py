
import time
from decimal import Decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def pause():
    time.sleep(0)
    


def login(driver):
    driver.get(BASE_URL)
    pause()

    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    pause()

    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    pause()

    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )
    pause()


def prepare_checkout(driver):
    login(driver)

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()
    pause()

    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()
    pause()

    driver.find_element(By.ID, "checkout").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-one.html")
    )
    pause()


def enter_customer_info(driver, first, last, postal):
    driver.find_element(By.ID, "first-name").send_keys(first)
    pause()

    driver.find_element(By.ID, "last-name").send_keys(last)
    pause()

    driver.find_element(By.ID, "postal-code").send_keys(postal)
    pause()


def continue_checkout(driver):
    driver.find_element(By.ID, "continue").click()
    pause()


def get_error_message(driver):
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )
    return error.text


def test_checkout_with_valid_information(driver):
    prepare_checkout(driver)

    enter_customer_info(driver, "Milan", "Dahal", "44600")
    continue_checkout(driver)

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-two.html")
    )

    assert "checkout-step-two.html" in driver.current_url


def test_checkout_missing_first_name(driver):
    prepare_checkout(driver)

    enter_customer_info(driver, "", "Dahal", "44600")
    continue_checkout(driver)

    error = get_error_message(driver)

    assert "First Name is required" in error


def test_checkout_missing_last_name(driver):
    prepare_checkout(driver)

    enter_customer_info(driver, "Milan", "", "44600")
    continue_checkout(driver)

    error = get_error_message(driver)

    assert "Last Name is required" in error


def test_checkout_missing_postal_code(driver):
    prepare_checkout(driver)

    enter_customer_info(driver, "Milan", "Dahal", "")
    continue_checkout(driver)

    error = get_error_message(driver)

    assert "Postal Code is required" in error


def test_order_overview_displays_product_and_prices(driver):
    prepare_checkout(driver)

    enter_customer_info(driver, "Milan", "Dahal", "44600")
    continue_checkout(driver)

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-two.html")
    )
    pause()

    product_names = [
        item.text for item in driver.find_elements(
            By.CLASS_NAME, "inventory_item_name"
        )
    ]

    assert "Sauce Labs Backpack" in product_names

    item_total = Decimal(
        driver.find_element(
            By.CLASS_NAME, "summary_subtotal_label"
        ).text.split("$")[1]
    )

    tax = Decimal(
        driver.find_element(
            By.CLASS_NAME, "summary_tax_label"
        ).text.split("$")[1]
    )

    total = Decimal(
        driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        ).text.split("$")[1]
    )

    assert item_total > 0
    assert tax >= 0
    assert total == item_total + tax


def test_complete_order_successfully(driver):
    prepare_checkout(driver)

    enter_customer_info(driver, "Milan", "Dahal", "44600")
    continue_checkout(driver)

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-two.html")
    )
    pause()

    driver.find_element(By.ID, "finish").click()
    pause()

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-complete.html")
    )

    confirmation = driver.find_element(
        By.CLASS_NAME, "complete-header"
    )

    assert confirmation.text == "Thank you for your order!"



def test_cancel_checkout_returns_to_cart(driver):
    prepare_checkout(driver)

    driver.find_element(By.ID, "cancel").click()
    pause()

    WebDriverWait(driver, 10).until(
        EC.url_contains("cart.html")
    )

    assert "cart.html" in driver.current_url

    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    product_names = [product.text for product in products]

    assert "Sauce Labs Backpack" in product_names
