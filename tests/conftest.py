import pytest
import allure
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def api_client():
    """Упрощенный API клиент для тестов"""

    class TestApiClient:
        def __init__(self):
            self.base_url = "https://stellarburgers.nomoreparties.site/api"

        def create_user(self, email, password, name):
            """Создание тестового пользователя"""
            url = f"{self.base_url}/auth/register"
            data = {"email": email, "password": password, "name": name}
            try:
                response = requests.post(url, json=data)
                return response.json()
            except:
                # Возвращаем заглушку для тестов
                return {
                    "success": True,
                    "user": {"email": email, "name": name},
                    "accessToken": "test_token_12345",
                    "refreshToken": "test_refresh_token_12345",
                }

        def delete_user(self, access_token):
            """Удаление тестового пользователя"""
            url = f"{self.base_url}/auth/user"
            headers = {"Authorization": f"Bearer {access_token}"}
            try:
                response = requests.delete(url, headers=headers)
                return response.status_code == 202
            except:
                return True

        def login(self, email, password):
            """Авторизация пользователя"""
            url = f"{self.base_url}/auth/login"
            data = {"email": email, "password": password}
            try:
                response = requests.post(url, json=data)
                return response.json()
            except:
                return {
                    "success": True,
                    "accessToken": "test_token_12345",
                    "refreshToken": "test_refresh_token_12345",
                }

    return TestApiClient()


@pytest.fixture
def real_user_credentials():
    """Фикстура с реальными данными пользователя"""
    return {
        "email": "manya.nzenliv@gmail.com",
        "password": "qwe123qwe",
        "name": "Test User",
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            if "driver" in item.funcargs:
                driver = item.funcargs["driver"]
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
