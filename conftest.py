import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BaseLocator
from locators.faq_locators import FaqLocator
from pages.base_page import BasePage
from pages.order_page import YaScooterOrder
from test_data import Urls


@pytest.fixture()
def page_order():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_PAGE)
    page_order = YaScooterOrder(driver)
    page_order.go_to_site_and_get_cookies()
    yield page_order
    driver.quit()


@pytest.fixture()
def page_ya_scooter():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_PAGE)
    page_ya_scooter = BasePage(driver)
    page_ya_scooter.go_to_site_and_get_cookies()
    yield page_ya_scooter
    driver.quit()
