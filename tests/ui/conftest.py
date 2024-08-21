import os

import pytest
from selene import browser

from allure import step


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    with step("Settings base url"):
        browser.config.base_url = "https://www.21vek.by/"
    with step("Setting up timeout for browser"):
        browser.config.timeout = 15
    with step("Setting up browser window size"):
        # browser.config.window_width = 1920
        # browser.config.window_height = 1200
        browser.driver.maximize_window()

    yield

    with step("Quit driver"):
        browser.quit()


