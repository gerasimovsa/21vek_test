from allure import step
from selene import browser, by, have, be, command


class VekFooter:
    def press_up_button(self):
        with step("Scroll down to footer"):
            browser.element(".styles_legalInformationBlock__iXOVK").should(be.visible).perform(
                command.js.scroll_into_view)
            browser.element(".style_upButtonLabel__LPAA4").click()
        return self
