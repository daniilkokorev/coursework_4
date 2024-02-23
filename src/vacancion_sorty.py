import json
from datetime import datetime
from pprint import pprint

from config import DATA

class VacancionsSort:
    """
    Класс сортирует список вакансий
    """
    def __init__(self):
        self.vacantion_sorty_list = []
        self.date_formated = None

    def vacation_sorted(self):
        # получаем отсортированный список вакансий из json файла
        with open(DATA, encoding='utf-8') as file:
            vacantions = json.load(file)
        for v in vacantions:
            # проверяет зарплату
            if v['salary']['from'] is None:
                v['salary']['from'] = 0
            elif v['salary']['to'] is None:
                v['salary']['to'] = 0
            elif v['published_at']:
                # форматирует дату вакансии в нужный формат
                date = datetime.strptime(v['published_at'], "%Y-%m-%dT%H:%M:%S+%f")
                self.date_formated = f"{date:%d.%m.%Y}"
            self.vacantion_sorty_list.append({
                "name_vacancion": v["name"],
                "salary_from": v["salary"]["from"],
                "salary_to": v["salary"]["to"],
                "city": v["area"]["name"],
                # требования
                "skill_t": v["snippet"]["requirement"],
                # ответственность
                "skill_o": v["snippet"]["responsibility"],
                "date": self.date_formated
            })
        return self.vacantion_sorty_list
