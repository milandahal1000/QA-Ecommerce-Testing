
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.test_data import BASE_URL
class LoginPage:

    URL = BASE_URL

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        time.sleep(0)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        time.sleep(0)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        time.sleep(0)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(0)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error.text