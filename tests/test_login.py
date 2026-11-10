import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


def pause():
    time.sleep(3)


def test_valid_login(driver):
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

    assert "inventory.html" in driver.current_url


def test_invalid_login(driver):
    driver.get(BASE_URL)
    pause()

    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    pause()

    driver.find_element(By.ID, "password").send_keys("wrong_password")
    pause()

    driver.find_element(By.ID, "login-button").click()
    pause()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert error.is_displayed()


def test_empty_login(driver):
    driver.get(BASE_URL)
    pause()

    driver.find_element(By.ID, "login-button").click()
    pause()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "Username is required" in error.text