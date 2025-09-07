from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@href, '/feed')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href, '/')]")

    TOTAL_ORDERS_COUNT = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p",
    )
    TODAY_ORDERS_COUNT = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p",
    )

    ORDER_FEED_ITEMS = (By.XPATH, "//li[contains(@class, 'OrderFeed_item__')]")
    IN_PROGRESS_SECTION = (
        By.XPATH,
        "//div[contains(text(), 'В работе')]/following-sibling::ul",
    )

    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    ORDER_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_close__')]")
