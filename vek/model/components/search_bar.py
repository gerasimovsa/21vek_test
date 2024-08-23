from allure import step
from selene import browser, by, have


class VekSearchBar:
    def search_catalog_item(self, query: str):
        with step(f"Enter {query} into the search bar"):
            browser.element("#catalogSearch").type(query).press_enter()
        return self
