
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.test_data import FIRST_NAME, LAST_NAME, POSTAL_CODE, BASE_URL

class CartPage:

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    
    def add_product(self, product_id):
        button = (By.ID, f"add-to-cart-{product_id}")
        self.driver.find_element(*button).click()
        time.sleep(0)


    def add_backpack(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()
        time.sleep(0)

    def open_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
        self.wait.until(EC.url_contains("cart.html"))
        time.sleep(0)

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def get_cart_product_names(self):
        items = self.driver.find_elements(*self.CART_PRODUCT_NAMES)
        return [item.text for item in items]

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_backpack(self):
        self.driver.find_element(*self.REMOVE_BACKPACK).click()
        time.sleep(0)

    def continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()
        self.wait.until(EC.url_contains("inventory.html"))
        time.sleep(0)
