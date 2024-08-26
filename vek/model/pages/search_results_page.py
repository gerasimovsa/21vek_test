from allure import step
from selene import browser, be, have, by, command


class VekSearchResultsPage:
    def set_price_range(self, min_price: str, max_price: str):
        with step("Fill min price filter"):
            browser.element("[name='min']").should(be.blank).type(min_price)
        with step("Fill max price filter"):
            browser.element("[name='max']").should(be.blank).type(max_price)
        with step("Wait until filters are updated"):
            browser.element("span.digi-filters__item").wait_until(be.visible)
        return self

    def enable_search_filter(self, filter_name: str):
        with step(f"Enabled {filter_name} filter"):
            browser.all("span.digi-facet-option__text").element_by(have.text(filter_name)).perform(
                command.js.scroll_into_view).click()
        return self

    def open_item_page(self, item: str):
        with step(f"Open {item} page"):
            browser.element(by.partial_text(item)).click()
        return self

    def should_have_catalog_results(self, product_quantity: int = None, product_labels: list[str] = None):
        if product_quantity:
            with step(f"Check item quantity is {product_quantity}"):
                browser.all(".ListingProduct_product__WBPsd").should(have.(product_quantity))
        if product_labels:
            with step(f"Check shown items are {product_labels}"):
                browser.all("[data-testid='card-info-a']").should(have.texts(product_labels))
        return self
