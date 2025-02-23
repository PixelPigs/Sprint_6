import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import *
from test_data import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.description('Перейти на сайт и принять куки')
    def go_to_site_and_get_cookies(self):
        self.driver.get(Urls.BASE_PAGE)
        return self.find_element_on_page(BaseLocator.COOKIE_BUTTON).click()

    @allure.description('Получить текущий урл')
    def check_url_page(self):
        return self.driver.current_url

    @allure.description('Ожидание загрузки страницы, проверяем, что элемент есть на странице')
    def check_wait_element(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    @allure.description('Найти элемент на странице')
    def find_element_on_page(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    @allure.description('Клик по кнопке Заказать')
    def order_on_button_top(self):
        self.find_element_and_click(BaseLocator.BUTTON_ORDER_TOP)
        return self.find_element_on_page(OrderLocator.TITLE_ORDER_FORM)

    @allure.description('Найти элемент и кликнуть по нему')
    def find_element_and_click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))
        return self.find_element_on_page(locator).click()

    @allure.title('Скролл до нужного элемента')
    @allure.description('Ожидание элемента, ищем элемент по локатору, проверяем что он кликабелен')
    def scroll_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
        element = self.find_element_on_page(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(element))

    def wait_new_window_and_switch(self):
        WebDriverWait(self.driver, 10).until(ec.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def wait_for_url_content(self, contains):
        WebDriverWait(self.driver, 10).until(ec.url_contains(contains))
