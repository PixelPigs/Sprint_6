import allure
import pytest
from selenium import webdriver

from locators.base_page_locators import *
from locators.order_page_locators import *
from test_data import Urls
from pages.order_page import *
from pages.base_page import *
from conftest import *


class TestOrder:

    @allure.title("Клик по 'Заказать' в шапке страницы")
    @allure.description("Находим кнопку в шапке, кликаем, сравниваем урл страницы и элемент")
    def test_check_button_top_for_order(self, page_order):
        page_order.find_element_and_click(BaseLocator.BUTTON_ORDER_TOP)
        assert page_order.check_url_page() == Urls.ORDER_PAGE and page_order.find_element_on_page(
            OrderLocator.TITLE_ORDER_FORM
        )

    @allure.title("Клик по 'Заказать' в середине страницы")
    @allure.description("Скролл до кнопки, кликаем, сравниваем урл страницы и элемент")
    def test_check_button_middle_for_order(self, page_order):
        page_order.scroll_to_element(BaseLocator.BUTTON_ORDER_MIDDLE)
        page_order.find_element_and_click(BaseLocator.BUTTON_ORDER_MIDDLE)
        assert page_order.check_url_page() == Urls.ORDER_PAGE and page_order.find_element_on_page(
            OrderLocator.TITLE_ORDER_FORM
        )

    # Проверяем создание заказа (можно проверить разные данные из test_data, class OrderFormData, подставить
    # индекс 0 или 1)
    @pytest.mark.parametrize('index', [0, 1])
    @allure.title("Проверяем сообщение успешного заказа")
    @allure.step("Заполняем форму Для кого самокат")
    @allure.step("клик Далее")
    @allure.step("Заполняем форму Про аренду")
    @allure.step("Клик Да (в поп-ап Хотите оформить заказ)")
    @allure.step("Проверяем что появился поп-ап Заказ оформлен")
    def test_check_order_1(self, page_order, index):
        page_order.order_on_button_top()
        page_order.enter_form_for_who_scooter(index)
        page_order.find_element_and_click(OrderLocator.NEXT_BUTTON)
        page_order.enter_form_about_rent(index)
        page_order.find_element_and_click(OrderLocator.ORDER_BUTTON_RENTAL_FORM)
        page_order.confirm_order_in_pop_up()
        assert page_order.find_element_on_page(OrderLocator.POP_UP_ORDER_PLACED)
