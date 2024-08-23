import allure
from allure_commons.types import Severity

from vek.model.pages.application import app


@allure.title("User registration test")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "POSITIVE")
@allure.feature("Registration")
@allure.story("Verify that user can register using an email")
@allure.link('https://www.21vek.by/', name="Main Page")
def test_email_registration():
    app.main_page.open()

    app.main_page.open_registration_modal()
    app.main_page.submit_registration_form("test_oz_001@gmail.com", "+375 (44) 582-16-20")
    app.main_page.accept_personal_data_terms()

    app.main_page.should_have_registration_successful()


@allure.title("User authorization exposes menus test")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "POSITIVE")
@allure.feature("Authorization")
@allure.story("Verify that authorization exposes user related menus")
@allure.link('https://www.21vek.by/', name="Main Page")
def test_email_authorization():
    app.main_page.open()
    app.main_page.open_auth_modal()
    app.main_page.submit_auth_form("gerasimov.ra9@gmail.com", "8d555bfe")
    app.main_page.close_add_phone_modal()
    app.main_page.should_have_account_menus_available(['Корзина',
                                                       'Мои заказы',
                                                       'Избранные товары',
                                                       'Списки сравнения',
                                                       'Просмотренные',
                                                       'Личные данные',
                                                       'Бонусный счет',
                                                       'Лист ожидания',
                                                       'Отзывы и вопросы',
                                                       'Выход'])


@allure.title("User data after authorization test")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "POSITIVE")
@allure.feature("Authorization")
@allure.story("Verify that user can authorize using credentials")
@allure.link('https://www.21vek.by/', name="Main Page")
def test_email_authorization_user_data():
    app.main_page.open()

    app.main_page.open_auth_modal()
    app.main_page.submit_auth_form("gerasimov.ra9@gmail.com", "8d555bfe")
    app.main_page.close_add_phone_modal()
    app.main_page.open_personal_data_page()

    app.personal_data_page.should_have_user_data("gerasimov.ra9@gmail.com",
                                                 "Sergey",
                                                 "Gerasimov",
                                                 "Мужской",
                                                 "16.12.1994")


@allure.title("User logout test")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "POSITIVE")
@allure.feature("Log out")
@allure.story("Verify that user log out")
@allure.link('https://www.21vek.by/', name="Main Page")
def test_log_out():
    app.main_page.open()

    app.main_page.open_auth_modal()
    app.main_page.submit_auth_form("gerasimov.ra9@gmail.com", "8d555bfe")
    app.main_page.close_add_phone_modal()
    app.main_page.user_log_out()

    app.main_page.should_have_user_logged_out()


@allure.title("User failed registration test")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "NEGATIVE")
@allure.feature("Registration")
@allure.story("Verify that user cannot register with used email")
@allure.link('https://www.21vek.by/', name="Main Page")
def test_failed_email_registration():
    app.main_page.open()

    app.main_page.open_registration_modal()
    app.main_page.submit_registration_form(email="test_oz_001@gmail.com", phone="445821620")

    app.main_page.should_have_check_email_message()


@allure.title("User failed authorization")
@allure.tag("ui")
@allure.severity(Severity.CRITICAL)
@allure.label("type", "NEGATIVE")
@allure.feature("Authorization")
@allure.story("Verify that failed authorization shows error")
@allure.link('https://www.21vek.by/', name="Main Page")
def test_failed_email_authorization():
    app.main_page.open()

    app.main_page.open_auth_modal()
    app.main_page.submit_auth_form("fake_email@gmail.com", "password")

    app.main_page.should_have_check_email_message()


