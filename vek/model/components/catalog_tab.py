from allure import step
from selene import browser, by, have


class VekCatalogTab:

    def open_catalog_category(self, category: str):
        with step("Open catalog"):
            browser.element(".styles_catalogButton__z9L_j").click()
        with step(f"Select {category} category"):
            browser.element(by.text(category)).click()
        return self

    def navigate_catalog_subcategory(self, category: str, subcategory: str):
        with step("Open catalog"):
            browser.element(".styles_catalogButton__z9L_j").click()
        with step(f"Select {category} category"):
            browser.element(by.text(category)).hover()
        with step(f"Got to {subcategory} category"):
            browser.element(by.text(subcategory)).click()
        return self

    def should_have_catalog_path(self, top_category: str, mid_category: str, subcategory: str):
        with step("Checking catalog path"):
            browser.all(".Breadcrumbs-module_crumb__cuqKz>a").should(
                have.exact_texts([mid_category, top_category, "Главная"]))
        with step("Checking opened subcategory"):
            browser.element("[data-testid='category-name']").should(have.exact_text(subcategory))
        return self
