from selenium.webdriver.common.by import By


class OrderLocator:
    TITLE_ORDER_FORM = By.XPATH, ".//div[@class= 'Order_Header__BZXOb' and text()='Для кого самокат']"
    # Локаторы для форм заказа
    NAME_FIELD = By.XPATH, ".//input[@placeholder='* Имя']"
    LAST_NAME_FILD = By.XPATH, ".//input[@placeholder='* Фамилия']"
    ADDRESS_FIELD = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    SUBWAY_FIELD = By.XPATH, ".//input[@placeholder='* Станция метро']"
    TELEPHONE_FIELD = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    DATE_FIELD = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    RENTAL_BUTTON = By.XPATH, "//div[text()='* Срок аренды']"
    COMMENT = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"
    COLOR = By.XPATH, ".//div[contains(@class, 'Order_Checkboxes__3lWSI')]"

    # Кнопка Далее, форма Для кого самокат
    NEXT_BUTTON = By.XPATH, ".//button[text()='Далее']"

    # Кнопка Заказать, форма Про аренду
    ORDER_BUTTON_RENTAL_FORM = By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']"

    # Поп-ап Хотите оформить заказ
    POP_UP_ORDER = By.XPATH, ".//div[text()='Хотите оформить заказ?']"
    YES_BUTTON = By.XPATH, ".//button[text()='Да']"

    # Поп-ап Заказ оформлен
    POP_UP_ORDER_PLACED = By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]"
