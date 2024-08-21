from allure import step
from selene import browser, be, by, have, command
from selenium.common import TimeoutException


class VekMainPage:

    @staticmethod
    def reject_cookies():
        with step('Reject cookies'):
            browser.element(".AgreementCookie_reject__f5oqP").should(be.visible).click()
            browser.element(".Button-module__gray-secondary").should(be.visible).click()

    def open(self):
        with step("Open www.vek.by page"):
            browser.open("/")
            self.reject_cookies()

    def open_account_menu(self):
        with step("Open account menu"):
            browser.element("[class='userToolsText']").should(be.visible).click()
        return self

    def open_personal_data_page(self):
        with step("Open personal data page"):
            self.open_account_menu()
            browser.element("[href='/profile/info/']").should(be.visible).click()
        return self

    def header_open_cart_page(self):
        with step("Open cart page from header"):
            browser.element(".headerCart").should(be.visible).click()
        return self

    def header_open_favorites_page(self):
        with step("Open favorites page from header"):
            browser.element(".headerFavoritesBox").should(be.visible).click()
        return self

    def search_catalog_item(self, query: str):
        with step(f"Enter {query} into the search bar"):
            browser.element("#catalogSearch").type(query).press_enter()
        return self

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

    def open_auth_modal(self):
        with step("Open auth window"):
            self.open_account_menu()
            browser.element("[class='Button-module__buttonText']>span").should(be.visible).click()
        return self

    def open_registration_modal(self):
        with step("Open registration window"):
            self.open_account_menu()
            browser.element("[class='Button-module__buttonText']>span").should(be.visible).click()
            browser.element("[class*='styles_secondaryAction__H7V7H']").should(be.visible).click()
        return self

    def submit_auth_form(self, email: str, password: str):
        with step("Fill emails and password fields"):
            browser.element("#login-email").should(be.blank).type(email)  # gerasimov.ra9@gmail.com
            browser.element("#login-password").should(be.blank).type(password)  # 8d555bfe
        with step("Submit authorization"):
            browser.element("[data-testid='loginSubmit']").click()
        return self

    def close_add_phone_modal(self):
        with step("Close add phone number window"):
            browser.element("[class*='BaseModalDesktop-module__modalOverlay'] path").should(be.visible).click()
        return self

    def submit_registration_form(self, email):
        with step("Fill email field"):
            browser.element("#register-email").should(be.blank).type(email)
        with step("Submit registration"):
            browser.element(".Form-module__submitContainer>button").click()
        return self

    def accept_personal_data_terms(self):
        with step("Agree personal data usage"):
            browser.element("[data-testid='agreeButton']").click()  # diagree - .Button-module__gray-secondary
        return self

    def user_log_out(self):
        with step("Log out user"):
            self.open_account_menu()
            browser.element("[href='/logout/']").should(be.visible).click()
        return self

    def change_location(self, location):
        with step("Change user location"):
            browser.element(".styles_localityBtn__qrGFQ").should(be.visible).click()
            browser.element("[class*='select__value-container']").should(be.present).click()
            browser.element(by.text(f"г. {location}")).should(be.visible).click()
            browser.element("[class*='style_baseActionButtonMargin__4haYC']").should(be.visible).click()
        return self

    def press_up_button(self):
        with step("Scroll down to footer"):
            browser.element(".styles_legalInformationBlock__iXOVK").should(be.visible).perform(
                command.js.scroll_into_view)
            browser.element(".style_upButtonLabel__LPAA4").click()
        return self

    def should_have_account_menus_available(self, menu_titles):
        with step("Check account menu items are available"):
            self.open_account_menu()
            browser.all(".ProfileItem_itemText__h3Pbr").should(have.exact_texts(menu_titles))
        return self

    def should_have_registration_successful(self):
        with step("Check success message"):
            browser.element(".SuccessScreen_successTitle__cCZL9").should(have.text("Вы зарегистрированы"))
        with step("Check enter button is visible"):
            browser.element("//div[text()='Войти']").should(be.visible)
        return self

    def should_have_user_logged_out(self):
        with step("Check user is logged out"):
            self.open_account_menu()
            browser.element("[data-testid='loginButton']").should(be.present)
            browser.element(".userToolsSubtitle").should(be.not_.present)
        return self

    def should_have_header_buttons(self):
        browser.all(".styles_promoItem__aolWq").should(be.present)
        browser.all(".styles_promoItem__aolWq").should(have.size(13))
        return self

    def should_have_location_set(self, location: str):
        with step("Check that location is set"):
            browser.element(".styles_localityBtn__qrGFQ").should(have.exact_text(f"г. {location}"))
        return self

