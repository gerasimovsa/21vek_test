from allure import step
from selene import browser, have, be


class VekPersonalDataPage:

    def should_have_user_data(self, email, first_name, last_name, gender, birth_date):
        full_name = first_name + " " + last_name
        with (step("Check name field")):
            browser.element(".styles_personalDataItemWrapper__ROsLu:nth-child(2) p:nth-child(2)"
                            ).should(have.text(full_name))
        with (step("Check gender field")):
            browser.element(".styles_personalDataItemWrapper__ROsLu:nth-child(3) p:nth-child(2)"
                            ).should(have.text(gender))
        with (step("Check birth data field")):
            browser.element(".styles_personalDataItemWrapper__ROsLu:nth-child(4) p:nth-child(2)"
                            ).should(have.text(birth_date))
        with (step("Check email field")):
            browser.element(".styles_personalDataEmailWrapper__jMKAP p:nth-child(2)"
                            ).should(have.text(email))
        return self


