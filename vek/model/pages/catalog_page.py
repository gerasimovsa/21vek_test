import allure
from selene import browser, have


class VekCatalogPage:

    def should_have_catalog_path(self, top_category: str, mid_category: str, subcategory: str):
        with allure.step("Checking catalog path"):
            browser.all(".Breadcrumbs-module_crumb__cuqKz>a").should(
                have.exact_texts([mid_category, top_category, "Главная"]))
        with allure.step("Checking opened subcategory"):
            browser.element("[data-testid='category-name']").should(have.exact_text(subcategory))
        return self
