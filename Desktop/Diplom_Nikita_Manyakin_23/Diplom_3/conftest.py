import pytest
from pages.base_page import BasePage
from selenium import webdriver


@pytest.fixture(scope="function", params=("chrome", "firefox"))
def driver(request):
    """Драйвер запуска Chrome и Firefox"""
    driver_name = request.param
    if driver_name == "chrome":
        driver = webdriver.Chrome()
    elif driver_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported driver: {driver_name}")
    driver.maximize_window()
    BasePage.set_driver(driver)
    yield driver
    driver.quit()
