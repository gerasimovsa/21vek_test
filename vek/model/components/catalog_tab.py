from allure import step
from selene import browser, by, have, be, command


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

    def set_price_range(self, min_price: int, max_price: int):
        with step("Setting min and max price filter"):
            browser.element("#minPrice").should(be.blank).type(str(min_price))
            browser.element("#maxPrice").should(be.blank).type(str(max_price))
        return self

    def enable_catalog_filters(self, *args):
        for label in args:
            with step(f"Enabling {label} catalog filter"):
                checkbox = browser.element(f"//span[text()='{label}']").should(be.visible)
                checkbox.perform(command.js.scroll_into_view)
                checkbox.click()
        return self

    def reset_all_filters(self):
        browser.element("[data-testid='reset-products-filters']").should(be.visible).click()
        return self

    def should_have_catalog_results(self, product_quantity: int = None, product_labels: list[str] = None):
        if product_quantity:
            with step(f"Check item quantity is {product_quantity}"):
                browser.all(".ListingProduct_product__WBPsd").should(have.size(product_quantity))
        if product_labels:
            with step(f"Check shown items are {product_labels}"):
                browser.all("[data-testid='card-info-a']").should(have.texts(product_labels))
        return self

    def should_have_filters_active(self, *args):
        with step(f"Check {args} filters are active"):
            browser.all("[aria-pressed='true'] span:nth-child(4)").should(have.texts(args))
        return self
