from allure import step
from selene import browser, by, have, be


class VekHeader:

    def header_open_cart_page(self):
        with step("Open cart page from header"):
            browser.element(".headerCart").should(be.visible).click()
        return self

    def header_open_favorites_page(self):
        with step("Open favorites page from header"):
            browser.element(".headerFavoritesBox").should(be.visible).click()
        return self

    def change_location(self, location):
        with step("Change user location"):
            browser.element(".styles_localityBtn__qrGFQ").should(be.visible).click()
            browser.element("[class*='select__value-container']").should(be.present).click()
            browser.element(by.text(f"г. {location}")).should(be.visible).click()
            browser.element("[class*='style_baseActionButtonMargin__4haYC']").should(be.visible).click()
        return self

    def should_have_header_buttons(self):
        browser.all(".styles_promoItem__aolWq").should(be.present)
        browser.all(".styles_promoItem__aolWq").should(have.size(13))
        return self

    def should_have_location_set(self, location: str):
        with step("Check that location is set"):
            browser.element(".styles_localityBtn__qrGFQ").should(have.exact_text(f"г. {location}"))
        return self
