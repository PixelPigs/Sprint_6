from selenium.webdriver.common.by import By


class BaseLocator:
    BUTTON_ORDER_TOP = By.XPATH, ".//button[@class= 'Button_Button__ra12g' and text()='Заказать']"
    BUTTON_ORDER_MIDDLE = By.XPATH, ".//button[@class= 'Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"
    COOKIE_BUTTON = By.XPATH, ".//button[text()='да все привыкли']"
    LOGO_SCOOTER = By.XPATH, ".//img[@alt='Scooter']/parent::a"
    LOGO_YANDEX = By.XPATH, ".//img[@alt='Yandex']/parent::a"
