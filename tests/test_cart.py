
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.cart_page import CartPage


def login_to_saucedemo(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )


def test_add_one_product_to_cart(driver):
    login_to_saucedemo(driver)

    cart = CartPage(driver)
    cart.add_backpack()

    assert cart.get_cart_count() == 1



def test_add_multiple_products_to_cart(driver):
    login_to_saucedemo(driver)

    cart = CartPage(driver)

    cart.add_product("sauce-labs-backpack")
    cart.add_product("sauce-labs-bike-light")

    assert cart.get_cart_count() == 2


def test_verify_cart_badge_count(driver):
    login_to_saucedemo(driver)

    cart = CartPage(driver)
    cart.add_backpack()

    assert cart.get_cart_count() == 1


def test_verify_products_in_cart(driver):
    login_to_saucedemo(driver)

    cart = CartPage(driver)
    cart.add_backpack()
    cart.open_cart()

    assert "Sauce Labs Backpack" in cart.get_cart_product_names()


def test_remove_product_from_cart(driver):
    login_to_saucedemo(driver)

    cart = CartPage(driver)
    cart.add_backpack()
    cart.open_cart()
    cart.remove_backpack()

    assert cart.get_cart_item_count() == 0


def test_continue_shopping_returns_to_inventory(driver):
    login_to_saucedemo(driver)

    cart = CartPage(driver)
    cart.add_backpack()
    cart.open_cart()
    cart.continue_shopping()

    assert "inventory.html" in driver.current_url
