import time

import allure
from allure_commons.types import Severity

from vek.model.pages.application import app


@allure.title("Change location in header")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "POSITIVE")
@allure.feature("Account menu")
@allure.story("Verify that user can change location on header")
@allure.link('https://www.21vek.by/', name="Header")
def test_header_change_location():
    app.main_page.open()

    app.header.change_location("Гомель")

    app.header.should_have_location_set("Гомель")


@allure.title("Clicking on 'up' button")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "POSITIVE")
@allure.feature("Account menu")
@allure.story("Verify that user scroll back to the header by clicking on 'up' button")
@allure.link('https://www.21vek.by/', name="Footer")
def test_footer_up_button():
    app.main_page.open()

    app.footer.press_up_button()

    app.header.should_have_header_buttons()


@allure.title("User navigate catalog test")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "POSITIVE")
@allure.feature("Catalog")
@allure.story("Verify that user can navigate a catalog subcategory")
@allure.link('https://www.21vek.by/', name="Catalog Page")
def test_navigate_catalog_category():
    app.main_page.open()

    app.catalog_tab.navigate_catalog_subcategory("Мебель", "Диваны")

    app.catalog_tab.should_have_catalog_path("Мебель", "Мебель для жилых комнат", "Диваны")


@allure.title("User filter catalog items")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "POSITIVE")
@allure.feature("Catalog")
@allure.story("Verify that user can filter a catalog")
@allure.link('https://www.21vek.by/', name="Catalog Page")
def test_filter_catalog():
    app.main_page.open()
    app.catalog_tab.navigate_catalog_subcategory("Мебель", "Диваны")

    app.catalog_tab.reset_all_filters()
    app.catalog_tab.set_price_range(800, 1200)
    app.catalog_tab.enable_catalog_filters("для офиса", "Ящик для белья", "желтый")
    app.footer.press_up_button()

    app.catalog_tab.should_have_catalog_results(3, [
        "Диван Лига Диванов Лига-020 стол слева / 118495L (микровельвет желтый/желтый/коричневый)",
        "Диван Лига Диванов Лига-020 стол справа / 118495 (микровельвет желтый/желтый/коричневый)",
        "Диван Лига Диванов Лига-019 / 118353 (микровельвет желтый/подушки желтый)"])
    app.catalog_tab.should_have_filters_active("для офиса", "Ящик для белья", "желтый")

