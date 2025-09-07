from selenium.webdriver.common.by import By


class MainLocators:
    # Кнопка личного кабинета
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account')]")

    # Логотип для проверки загрузки
    LOGO = (
        By.XPATH,
        "//div[contains(@class, 'AppHeader_header__logo')] | //svg[contains(@class, 'logo')]",
    )

    # Кнопки конструктора
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//a[contains(@href, '/') and contains(@class, 'AppHeader_header__link')]",
    )
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@href, '/feed')]")
