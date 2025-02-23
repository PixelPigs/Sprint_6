from selenium.webdriver.common.by import By


class OrderLocator:
    TITLE_ORDER_FORM = By.XPATH, ".//div/div[2]/div[1][text()='Для кого самокат']"
    # Локаторы для форм заказа
    NAME_FIELD = By.XPATH, ".//div/div[2]/div[2]/div[1]/input"
    LAST_NAME_FILD = By.XPATH, ".//div/div[2]/div[2]/div[2]/input"
    ADDRESS_FIELD = By.XPATH, ".//div/div[2]/div[2]/div[3]/input"
    SUBWAY_FIELD = By.XPATH, ".//div/div[2]/div[2]/div[4]/div/div/input"
    TELEPHONE_FIELD = By.XPATH, ".//div/div[2]/div[2]/div[5]/input"
    DATE_FIELD = By.XPATH, ".//div[2]/div[2]/div[1]/div/div/input"
    RENTAL_BUTTON = By.XPATH, ".//div[2]/div[2]/div[2]/div/div[1]"
    COMMENT = By.XPATH, ".//div[2]/div[2]/div[4]/input"
    COLOR = By.XPATH, ".//div[2]/div[2]/div[3][contains(@class, 'Order_Checkboxes__3lWSI')]"

    # Кнопка Далее, форма Для кого самокат
    NEXT_BUTTON = By.XPATH, ".//div/div[2]/div[3]/button[text()='Далее']"

    # Кнопка Заказать, форма Про аренду
    ORDER_BUTTON_RENTAL_FORM = By.XPATH, ".//div[2]/div[3]/button[text()='Заказать']"

    # Поп-ап Хотите оформить заказ
    POP_UP_ORDER = By.XPATH, ".//div[2]/div[5]/div[1][text()='Хотите оформить заказ?']"
    YES_BUTTON = By.XPATH, ".//div[2]/div[5]/div[2]/button[text()='Да']"

    # Поп-ап Заказ оформлен
    POP_UP_ORDER_PLACED = By.XPATH, ".//div[2]/div[5]/div[1][contains(text(), 'Заказ оформлен')]"
