from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    ACTIVE_PASSWORD_FIELD = (
        By.XPATH,
        "//input[@name='Введите новый пароль' and contains(@class, 'input__textfield-focused')]",
    )
    CANCEL_BUTTON = (
        By.XPATH,
        "//a[text()='Войти']",
    )  # Кнопка отмены обычно ведет на вход
