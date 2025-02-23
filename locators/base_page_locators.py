from selenium.webdriver.common.by import By


class BaseLocator:
    BUTTON_ORDER_TOP = By.XPATH, ".//div[1]/div[2]/button[text()='Заказать']"
    BUTTON_ORDER_MIDDLE = By.XPATH, ".//div[4]/div[2]/div[5]/button[text()='Заказать']"
    COOKIE_BUTTON = By.XPATH, ".//button[text()='да все привыкли']"
    LOGO_SCOOTER = By.XPATH, ".//img[@alt='Scooter']/parent::a"
    LOGO_YANDEX = By.XPATH, ".//img[@alt='Yandex']/parent::a"
