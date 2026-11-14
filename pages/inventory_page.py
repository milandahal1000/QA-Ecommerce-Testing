
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.test_data import FIRST_NAME, LAST_NAME, POSTAL_CODE


class InventoryPage:

    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_products(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_NAMES)
        )

    def get_product_names(self):
        products = self.wait_for_products()
        time.sleep(0)
        return [product.text for product in products]

    def get_product_prices(self):
        prices = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(price.text.replace("$", "")) for price in prices]

    def sort_by_name_a_to_z(self):
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        Select(dropdown).select_by_value("az")
        time.sleep(0)

    def sort_by_price_low_to_high(self):
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        Select(dropdown).select_by_value("lohi")
        time.sleep(0)
