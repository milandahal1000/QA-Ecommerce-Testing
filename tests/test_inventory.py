import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def pause():
    time.sleep(3)

def login(driver):
    driver.get(BASE_URL)
    pause()

    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    pause()

    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    pause()

    driver.find_element(By.ID, "login-button").click()
    pause()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )


def get_product_names(driver):
    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )
    return [product.text for product in products]


def test_inventory_page_loads(driver):
    login(driver)

    assert "inventory.html" in driver.current_url

    title = driver.find_element(
        By.CLASS_NAME, "title"
    )

    assert title.text == "Products"


def test_all_products_are_displayed(driver):
    login(driver)

    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    pause()

    assert len(products) == 6


def test_product_names_are_not_empty(driver):
    login(driver)

    names = get_product_names(driver)
    pause()

    assert len(names) > 0
    assert all(name.strip() for name in names)


def test_product_prices_are_valid(driver):
    login(driver)

    prices = driver.find_elements(
        By.CLASS_NAME, "inventory_item_price"
    )

    pause()

    assert len(prices) > 0

    for price in prices:
        value = float(price.text.replace("$", ""))
        assert value > 0


def test_sort_products_name_a_to_z(driver):
    login(driver)

    sort_dropdown = Select(
        driver.find_element(
            By.CLASS_NAME, "product_sort_container"
        )
    )

    sort_dropdown.select_by_value("az")
    pause()

    actual_names = get_product_names(driver)
    expected_names = sorted(actual_names)

    assert actual_names == expected_names


def test_sort_products_price_low_to_high(driver):
    login(driver)

    sort_dropdown = Select(
        driver.find_element(
            By.CLASS_NAME, "product_sort_container"
        )
    )

    sort_dropdown.select_by_value("lohi")
    pause()

    price_elements = driver.find_elements(
        By.CLASS_NAME, "inventory_item_price"
    )

    actual_prices = [
        float(price.text.replace("$", ""))
        for price in price_elements
    ]

    expected_prices = sorted(actual_prices)

    assert actual_prices == expected_prices
