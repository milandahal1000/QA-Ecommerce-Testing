
import pytest
import time
import re
from pathlib import Path
from selenium import webdriver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def driver(request):
   
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument(
        "--disable-features=PasswordLeakDetection,PasswordCheck"
    )

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
    )


    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)

    yield browser

    # Capture a screenshot if the test fails
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_dir = Path("reports/screenshots")
        screenshot_dir.mkdir(parents=True, exist_ok=True)

        safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", request.node.nodeid)
        screenshot_path = screenshot_dir / f"{safe_name}.png"

        browser.save_screenshot(str(screenshot_path))
        print(f"\nFailure screenshot saved: {screenshot_path}")

    time.sleep(3)
    browser.quit()
