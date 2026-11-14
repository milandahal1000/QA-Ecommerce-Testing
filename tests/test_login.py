
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.test_data import VALID_USERNAME, VALID_PASSWORD,INVALID_USERNAME, INVALID_PASSWORD

from pages.login_page import LoginPage


def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USERNAME, VALID_PASSWORD)

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    assert "inventory.html" in driver.current_url


def test_invalid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login(INVALID_USERNAME, INVALID_PASSWORD)

    assert "Username and password do not match" in (
        login.get_error_message()
    )


def test_empty_login(driver):
    login = LoginPage(driver)
    login.open()
    login.click_login()

    assert "Username is required" in login.get_error_message()
