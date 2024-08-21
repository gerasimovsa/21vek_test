import time

import allure
from allure_commons.types import Severity

from vek.model.pages.application import app


@allure.title("User navigate catalog test")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "POSITIVE")
@allure.feature("Catalog")
@allure.story("Verify that user can navigate a catalog subcategory")
@allure.link('https://www.21vek.by/', name="Catalog Page")
def test_navigate_catalog_category():
    app.main_page.open()

    app.main_page.navigate_catalog_subcategory("Мебель", "Диваны")

    app.catalog_page.should_have_catalog_path("Мебель", "Мебель для жилых комнат", "Диваны")


@allure.title("User navigate catalog test")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "POSITIVE")
@allure.feature("Catalog")
@allure.story("Verify that user can navigate a catalog subcategory")
@allure.link('https://www.21vek.by/', name="Catalog Page")
def test_filter_catalog():
    app.main_page.open()

    app.main_page.navigate_catalog_subcategory("Мебель", "Диваны")

    app.catalog_page.should_have_catalog_path("Мебель", "Мебель для жилых комнат", "Диваны")