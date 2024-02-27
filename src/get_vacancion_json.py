import json
import os
from pprint import pprint

from src.get_vacancies_hh_api import GetvacanciesHHAPI
from src.abstract_json import AbstractJson
from config import DATA


class GetVacancionJson(GetvacanciesHHAPI, AbstractJson):
    """
    Класс для работы с файлом
    """

    def vacancion_json_write(self):
        """
        Записывает вакансии в файл json
        """
        with open(DATA, 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.get_vacancies_hh_api, indent=4, ensure_ascii=False))

    @property
    def vacancion_json_append(self):
        """
        Добавляет вакансии в файл json
        """
        with open(DATA, encoding='utf-8') as json_file:
            vacantion_json_list = json.load(json_file)
        vacantion_json_list.extend(self.get_vacancies_hh_api)
        with open(DATA, 'w', encoding='utf-8') as file_app:
            json.dump(vacantion_json_list, file_app, indent=4, ensure_ascii=False)
        return vacantion_json_list

    def vacancion_json_clear(self):
        """
        Удаляет данные из файла
        :return:
        """
        with open(DATA, 'w', encoding='utf-8') as clear_file:
            del clear_file


if __name__ == '__main__':
    v = GetVacancionJson('python', 1)
    pprint(v.vacancion_json_append)
