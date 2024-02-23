import json
import requests
from src.abstract_hh_api import AbstractHHAPI
from config import DATA
from src.vacantions_names import Vacancions


class GetvacanciesHHAPI(AbstractHHAPI, Vacancions):
    """
    Класс получает список вакансий по API с HH.ru и записывает в json файл
    """
    def __init__(self, name_vacancion, page_vacancion):
        super().__init__(name_vacancion, page_vacancion)

    def get_vacancies_hh_api(self):
        # получает список вакансий с HH по API
        key_response = {'text': self.name_vacancion, 'area': 113, 'per_page': self.page_vacancion,
                        'only_with_salary': "true"}
        response_vacancions = requests.get(f'https://api.hh.ru/vacancies', key_response).json()
        return response_vacancions

    def write_vacancions_list(self):
        # записывает вакансии в файл json
        with open(DATA, 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.get_vacancies_hh_api(), indent=4, ensure_ascii=False))
