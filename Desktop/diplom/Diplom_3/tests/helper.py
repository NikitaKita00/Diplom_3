import allure
import string
import random
import requests
from data import API_HOST
from pages.account_page import AccounttPage
from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage


@allure.step("Регистрация нового пользователя (через API)")
def register_new_user():
    def _generate_random_string(length):
        return "".join(random.choice(string.ascii_lowercase) for i in range(length))

    email = _generate_random_string(12) + "@test.do"
    password = _generate_random_string(10)
    name = _generate_random_string(12)
    requests.post(
        API_HOST + "/api/auth/register",
        json={"email": email, "password": password, "name": name},
    )
    return email, password, name


@allure.step("Вход от имени зарегистрированного пользователя")
def login(email, password):
    main_page = MainPage()
    main_page.open()
    main_page.cabinet_button.click()
    AccounttPage().login(email, password)
    ConstructorPage().check_is_present()


def register_and_login():
    email, password, _ = register_new_user()
    login(email, password)
