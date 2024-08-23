import allure
from selene import browser, be, have, by, command


class VekSearchResultsPage:
    def set_price_range(self, min_price: str, max_price: str):
        with allure.step("Fill min price filter"):
            browser.element("[name='min']").should(be.blank).type(min_price)
        with allure.step("Fill max price filter"):
            browser.element("[name='max']").should(be.blank).type(max_price)
        with allure.step("Wait until filters are updated"):
            browser.element("span.digi-filters__item").wait_until(be.visible)
        return self

    def enable_search_filter(self, filter_name: str):
        with allure.step(f"Enabled {filter_name} filter"):
            browser.all("span.digi-facet-option__text").element_by(have.text(filter_name)).perform(
                command.js.scroll_into_view).click()
        return self

    def open_item_page(self, item: str):
        with allure.step(f"Open {item} page"):
            browser.element(by.partial_text(item)).click()
        return self

    def should_have_search_results(self, product_quantity: int = None, product_labels: list[str] = None):
        if product_quantity:
            with allure.step(f"Check item quantity is {product_quantity}"):
                browser.element("#j-filter__counter").should(have.exact_text(str(product_quantity)))
        if product_labels:
            with allure.step(f"Check shown items are {product_labels}"):
                browser.all(".result__name").should(have.exact_texts(product_labels))
        return self

    def should_have_filters_active(self, *args):
        with allure.step(f"Check {args} filters are activee"):
            browser.all("span.digi-filters__item-value").should(have.texts(args))
        return self
