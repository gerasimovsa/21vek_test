from allure import step
from selene import browser, be, by, have, command
from selene.core.exceptions import TimeoutException


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

    def open_auth_modal(self):
        with step("Open auth window"):
            self.open_account_menu()
            browser.element("[class='Button-module__buttonText']>span").should(be.visible).click()
        return self

    def open_registration_modal(self):
        with step("Open registration window"):
            self.open_account_menu()
            browser.element("[class='Button-module__buttonText']>span").should(be.visible).click()
            browser.element(by.text("Регистрация")).should(be.visible).click()
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

    def accept_personal_data_terms(self):
        with step("Agree personal data usage"):
            browser.element("[data-testid='agreeButton']").click()  # diagree - .Button-module__gray-secondary
        return self

    def submit_registration_form(self, email, phone=None):
        try:
            with step("Fill phone field"):
                browser.element("[label='Номер телефона']").type(phone)
            with step("Fill email field"):
                browser.element("[label='Электронная почта']").type(email)
            with step("Press continue and accept terms"):
                browser.element("[class*='RegistrationFormNew_submit__9xq36']").click()
                self.accept_personal_data_terms()
        except TimeoutException:
            with step("Fill email field"):
                browser.element("#register-email").should(be.blank).type(email)
            with step("Submit registration"):
                browser.element(".Form-module__submitContainer>button").click()
        return self

    def user_log_out(self):
        with step("Log out user"):
            self.open_account_menu()
            browser.element("[href='/logout/']").should(be.visible).click()
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

    def should_have_check_email_message(self):
        try:
            browser.element(".styles_errorText__LEN7M").should(be.present)
            browser.element(".styles_errorText__LEN7M").should(have.text("Проверьте электронную почту"))
        except TimeoutException:
            browser.element(".ErrorMessageLink_container__7D0yM").should(be.present)
            browser.element(".ErrorMessageLink_container__7D0yM").should(have.text("Проверьте электронную почту"))
        return self
