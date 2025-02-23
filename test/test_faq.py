import allure
import pytest

from selenium import webdriver
from test_data import FormFAQ
from test_data import Urls
from pages.faq_page import *
from pages.base_page import *
from locators.faq_locators import *
from locators.base_page_locators import *
from conftest import *


class TestYaScooterFAQ:

    # Тест сравнение ответов на вопросы с ожидаемым текстом, использовали параметризацию для упрощения проверки
    @allure.title('Проверяем текст каждого ответа по вопросу в блоке "Вопросы о важном"')
    @allure.description(
        'Переход на главную страницу сервиса, скрол к элементу формы Вопросы,'
        'Проверили, что вопрос кликабелен, Клик на вопрос, нашли текст ответа,'
        'сравнили с ожидаемым ответом'
    )
    @pytest.mark.parametrize(
        "question_number,answer,expected_answer",
        [
            (0, 0, FormFAQ.answer_1),
            (1, 1, FormFAQ.answer_2),
            (2, 2, FormFAQ.answer_3),
            (3, 3, FormFAQ.answer_4),
            (4, 4, FormFAQ.answer_5),
            (5, 5, FormFAQ.answer_6),
            (6, 6, FormFAQ.answer_7),
            (7, 7, FormFAQ.answer_8),
        ],
    )
    def test_check_answer_for_questions(self, page_faq, question_number, answer, expected_answer):
        page_faq.click_on_question(question_number)
        actual_answer = page_faq.get_answer_for_question(answer)
        assert actual_answer == expected_answer
