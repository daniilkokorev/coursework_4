import json

import requests

from config import DATA
from src.abstract_hh_api import AbstractHHAPI
from src.vacantions_names import Vacancions


class GetvacanciesHHAPI(AbstractHHAPI, Vacancions):
    """
    Класс получает список вакансий по API с HH.ru и записывает в json файл
    """
    def __init__(self, name_vacancion, page_vacancion):
        super().__init__(name_vacancion, page_vacancion)
        self.url_hh = 'https://api.hh.ru/'

    @property
    def get_vacancies_hh_api(self):
        """
        получает список вакансий с HH по API
        """
        key_response = {'text': self.name_vacancion, 'area': 113, 'per_page': self.page_vacancion,
                        'only_with_salary': "true"}
        response_vacancions = requests.get(f'{self.url_hh}vacancies', key_response).json()['items']
        return response_vacancions

    # def vacancion_json_write(self):
    #     """
    #     Записывает вакансии в файл json
    #     """
    #     with open(DATA, 'a', encoding='utf-8') as file:
    #         file.write(json.dumps(self.get_vacancies_hh_api, indent=4, ensure_ascii=False))
