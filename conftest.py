import pytest
import time
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)

    # Make every Selenium action pause for 3 seconds
    browser.implicitly_wait(3)

    yield browser

    time.sleep(3)  # Keep the final page visible before closing
    browser.quit()