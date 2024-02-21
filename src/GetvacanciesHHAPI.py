import json
from pprint import pprint

import requests
from AbstractHHAPI import AbstractHHAPI
from config import DATA


class GetvacanciesHHAPI(AbstractHHAPI):
    """
    Класс получает список вакансий по API с HH.ru и записывает в json файл
    """

    def __init__(self, name_vacancion: str):
        self.name_vacancion: str = name_vacancion
        self.message = "Найденные вакансии"
        self.list_vacancions = self.get_vacancies_hh_api()

    def __rep__(self):
        return self.list_vacancions

    def get_vacancies_hh_api(self) -> str:
        # получает список вакансий с HH по API
        if isinstance(self.name_vacancion, str):
            key_response = {'text': self.name_vacancion, 'area': 113, 'per_page': 100}
            response_vacancions = requests.get(f'https://api.hh.ru/vacancies', key_response)
            return response_vacancions.json()['items']
        else:
            self.message = "Вакансии не найдены"
            return self.message

    def write_vacancions_list(self):
        # записывает вакансии в файл json
        with open(DATA, 'w', encoding='utf-8') as file:
            json.dump(self.list_vacancions, file)
            return self.list_vacancions
