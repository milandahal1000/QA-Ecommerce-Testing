
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def pause():
    time.sleep(1)


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


def add_product(driver, product_id):
    driver.find_element(
        By.ID, f"add-to-cart-{product_id}"
    ).click()
    pause()


def open_cart(driver):
    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("cart.html")
    )
    pause()


def test_add_one_product_to_cart(driver):
    login(driver)

    add_product(driver, "sauce-labs-backpack")

    badge = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert badge.text == "1"


def test_add_multiple_products_to_cart(driver):
    login(driver)

    add_product(driver, "sauce-labs-backpack")
    add_product(driver, "sauce-labs-bike-light")

    badge = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert badge.text == "2"


def test_verify_cart_badge_count(driver):
    login(driver)

    add_product(driver, "sauce-labs-backpack")
    add_product(driver, "sauce-labs-bike-light")
    add_product(driver, "sauce-labs-bolt-t-shirt")

    badge = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert badge.text == "3"


def test_verify_products_in_cart(driver):
    login(driver)

    add_product(driver, "sauce-labs-backpack")
    add_product(driver, "sauce-labs-bike-light")

    open_cart(driver)

    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    product_names = [product.text for product in products]

    assert "Sauce Labs Backpack" in product_names
    assert "Sauce Labs Bike Light" in product_names
    assert len(product_names) == 2


def test_remove_product_from_cart(driver):
    login(driver)

    add_product(driver, "sauce-labs-backpack")
    add_product(driver, "sauce-labs-bike-light")

    open_cart(driver)

    driver.find_element(
        By.ID, "remove-sauce-labs-backpack"
    ).click()
    pause()

    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    product_names = [product.text for product in products]

    assert "Sauce Labs Backpack" not in product_names
    assert "Sauce Labs Bike Light" in product_names
    assert len(product_names) == 1


def test_continue_shopping_returns_to_inventory(driver):
    login(driver)

    add_product(driver, "sauce-labs-backpack")
    open_cart(driver)

    driver.find_element(
        By.ID, "continue-shopping"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )
    pause()

    assert "inventory.html" in driver.current_url
