
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.test_data import VALID_USERNAME, VALID_PASSWORD

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def login_to_saucedemo(driver):
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USERNAME, VALID_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )


def test_inventory_page_loads(driver):
    login_to_saucedemo(driver)

    assert "inventory.html" in driver.current_url


def test_all_products_are_displayed(driver):
    login_to_saucedemo(driver)

    inventory = InventoryPage(driver)
    products = inventory.get_product_names()

    assert len(products) > 0


def test_product_names_are_not_empty(driver):
    login_to_saucedemo(driver)

    inventory = InventoryPage(driver)
    products = inventory.get_product_names()

    assert all(name.strip() for name in products)


def test_product_prices_are_valid(driver):
    login_to_saucedemo(driver)

    inventory = InventoryPage(driver)
    prices = inventory.get_product_prices()

    assert len(prices) > 0
    assert all(price > 0 for price in prices)


def test_sort_products_name_a_to_z(driver):
    login_to_saucedemo(driver)

    inventory = InventoryPage(driver)
    inventory.sort_by_name_a_to_z()

    names = inventory.get_product_names()

    assert names == sorted(names)


def test_sort_products_price_low_to_high(driver):
    login_to_saucedemo(driver)

    inventory = InventoryPage(driver)
    inventory.sort_by_price_low_to_high()

    prices = inventory.get_product_prices()

    assert prices == sorted(prices)
