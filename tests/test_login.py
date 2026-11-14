
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    assert "inventory.html" in driver.current_url


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("invalid_user", "wrong_password")

    assert "Username and password do not match" in (
        login.get_error_message()
    )


def test_empty_login(driver):
    login = LoginPage(driver)
    login.open()
    login.click_login()

    assert "Username is required" in login.get_error_message()
