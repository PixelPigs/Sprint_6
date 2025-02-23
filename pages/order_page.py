import allure
from selenium.webdriver.common.by import By
from pages.base_page import *
from locators.base_page_locators import *
from locators.order_page_locators import *


class YaScooterOrder(BasePage):

    @allure.description('Выбрать поле Метро')
    def enter_street(self, street_name):
        self.find_element_and_click(OrderLocator.SUBWAY_FIELD)
        street = By.XPATH, f".//div[2]/div[2]/div[4]/div/div[2]/ul/li/button/div[2][contains(text(), '{street_name}')]"
        self.find_element_and_click(street)

    @allure.description('Найти поле на странице')
    def find_element_and_send_keys(self, locator, test_data):
        return self.find_element_on_page(locator).send_keys(test_data)

    @allure.description('Выбрать срок аренды')
    def enter_rental_period(self, rental_period):
        self.find_element_and_click(OrderLocator.RENTAL_BUTTON)
        rental_period = By.XPATH, f".//div[2]/div[2]/div[2]/div[2]/div[contains(text(), '{rental_period}')]"
        self.find_element_and_click(rental_period)

    @allure.description('Выбрать цвет самоката')
    def enter_color(self, color):
        self.check_wait_element(OrderLocator.COLOR)
        color = By.XPATH, f"./html/body/div/div/div[2]/div[2]/div[3]/label[contains(text(), '{color}')]"
        self.find_element_and_click(color)

    @allure.description('Проверить всплывающее окно и клик Подтвердить заказ')
    # Подтверждение заказа (поп-ап Хотите оформить заказ)
    def confirm_order_in_pop_up(self):
        self.find_element_on_page(OrderLocator.POP_UP_ORDER)
        self.find_element_and_click(OrderLocator.YES_BUTTON)

    @allure.description('Заполнить форму Для кого самокат')
    def enter_form_for_who_scooter(self, index):
        locators = OrderFormData.form_1
        for loc, text in locators.items():
            self.find_element_and_send_keys(loc, text[index])
        self.enter_street(OrderFormData.street[index])

    @allure.description('Заполнить форму Про аренду')
    def enter_form_about_rent(self, index):
        locators = OrderFormData.form_2
        for loc, text in locators.items():
            self.find_element_and_send_keys(loc, text[index])
        self.enter_color(OrderFormData.color[index])
        self.enter_rental_period(OrderFormData.rental_period[index])
