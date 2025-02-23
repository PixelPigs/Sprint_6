import allure
from selenium.webdriver.common.by import By
from pages.base_page import *
from locators.faq_locators import *


class YaScooterFAQ(BasePage):

    # Кликаем на кнопку вопроса, найдя вопрос по локатору
    @allure.step('Получить локатор кнопки вопроса, к общему локатору кнопок добавили порядковый номер')
    @allure.step('Ожидаем и находим элемент')
    @allure.step('Нажимаем на вопрос')
    def click_on_question(self, question_number: int):
        question_locator = By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"
        return self.find_element_and_click(question_locator)

    # Находим локатор ответа (отсчет с 0)
    @allure.step('Получить локатор кнопки ответа, к общему локатору кнопок добавили порядковый номер')
    @allure.step('Ожидаем и находим элемент')
    @allure.step('Получаем текст Ответа')
    def get_answer_for_question(self, answer_number: int):
        answer_locator = By.XPATH, f".//div[@id='accordion__panel-{answer_number}']/p"
        answer_text = self.find_element_on_page(answer_locator)
        return answer_text.text

