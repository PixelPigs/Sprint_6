import pytest
from selenium import webdriver
import allure

from locators.base_page_locators import *
from locators.order_page_locators import *
from test_data import Urls
from pages.order_page import *
from pages.base_page import *
from conftest import *


class TestHomePage:

    @allure.title('Проверка клик на Самокат в шапке страницы, переход на домашнюю страницу Я.Самокат')
    def test_check_click_scooter_go_to_base_page(self, page_ya_scooter):
        page_ya_scooter.order_on_button_top()
        page_ya_scooter.find_element_and_click(BaseLocator.LOGO_SCOOTER)
        assert page_ya_scooter.check_url_page() == Urls.BASE_PAGE

    @allure.title('Проверка клик на Яндекс в шапке страницы, редирект на страницу Я.Дзен')
    @allure.step('Нажать на кнопку Заказать - перейти на страницу Заказа')
    @allure.step('Нажать на лого Яндекс')
    @allure.step('Дождаться появления новой вкладки')
    @allure.step('Получаем список окон')
    @allure.step('Перейти на вторую вкладку')
    @allure.step('Дождаться ключевого слова в текущем урле')
    def test_check_click_yandex_open_new_window_dzen(self, page_ya_scooter):
        page_ya_scooter.order_on_button_top()
        page_ya_scooter.find_element_and_click(BaseLocator.LOGO_YANDEX)
        WebDriverWait(page_ya_scooter.driver, 10).until(ec.number_of_windows_to_be(2))
        windows = page_ya_scooter.driver.window_handles
        page_ya_scooter.driver.switch_to.window(windows[1])
        WebDriverWait(page_ya_scooter.driver, 10).until(ec.url_contains('dzen'))
        assert Urls.DZEN_PAGE in page_ya_scooter.check_url_page()
