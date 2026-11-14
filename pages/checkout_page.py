
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.test_data import FIRST_NAME, LAST_NAME, POSTAL_CODE


class CheckoutPage:

    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        self.wait.until(EC.url_contains("checkout-step-one.html"))
        time.sleep(0)

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        time.sleep(0)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        time.sleep(0)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        time.sleep(0)

    def enter_customer_information(self, first, last, postal):
        self.enter_first_name(first)
        self.enter_last_name(last)
        self.enter_postal_code(postal)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        time.sleep(0)

    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error.text

    def get_product_names(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_NAMES)
        )
        return [product.text for product in products]

    def get_subtotal(self):
        return self.driver.find_element(*self.SUBTOTAL).text

    def get_tax(self):
        return self.driver.find_element(*self.TAX).text

    def get_total(self):
        return self.driver.find_element(*self.TOTAL).text

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))
        time.sleep(0)

    def get_confirmation_message(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).text

    def click_cancel(self):
        self.driver.find_element(*self.CANCEL_BUTTON).click()
        self.wait.until(EC.url_contains("cart.html"))
        time.sleep(0)
