
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def prepare_checkout(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    cart = CartPage(driver)
    cart.add_backpack()
    cart.open_cart()

    checkout = CheckoutPage(driver)
    checkout.click_checkout()

    return checkout


def test_checkout_with_valid_information(driver):
    checkout = prepare_checkout(driver)

    checkout.enter_customer_information(
        "Milan", "Dahal", "44600"
    )
    checkout.click_continue()

    assert "checkout-step-two.html" in driver.current_url


def test_checkout_missing_first_name(driver):
    checkout = prepare_checkout(driver)

    checkout.enter_customer_information(
        "", "Dahal", "44600"
    )
    checkout.click_continue()

    assert "First Name is required" in checkout.get_error_message()


def test_checkout_missing_last_name(driver):
    checkout = prepare_checkout(driver)

    checkout.enter_customer_information(
        "Milan", "", "44600"
    )
    checkout.click_continue()

    assert "Last Name is required" in checkout.get_error_message()


def test_checkout_missing_postal_code(driver):
    checkout = prepare_checkout(driver)

    checkout.enter_customer_information(
        "Milan", "Dahal", ""
    )
    checkout.click_continue()

    assert "Postal Code is required" in checkout.get_error_message()


def test_order_overview_displays_product_and_prices(driver):
    checkout = prepare_checkout(driver)

    checkout.enter_customer_information(
        "Milan", "Dahal", "44600"
    )
    checkout.click_continue()

    assert "Sauce Labs Backpack" in checkout.get_product_names()
    assert "$29.99" in checkout.get_subtotal()
    assert "Tax:" in checkout.get_tax()
    assert "Total:" in checkout.get_total()


def test_complete_order_successfully(driver):
    checkout = prepare_checkout(driver)

    checkout.enter_customer_information(
        "Milan", "Dahal", "44600"
    )
    checkout.click_continue()
    checkout.click_finish()

    assert checkout.get_confirmation_message() == "Thank you for your order!"


def test_cancel_checkout_returns_to_cart(driver):
    checkout = prepare_checkout(driver)

    checkout.click_cancel()

    assert "cart.html" in driver.current_url
    assert "Sauce Labs Backpack" in checkout.get_product_names()
