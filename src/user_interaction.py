from src.input_user_error import InputUserError
from src.json_user_error import JsonUserError
from src.vacancion_sorty import VacancionsSort
from src.get_vacancies_hh_api import GetvacanciesHHAPI
from src.get_vacancion_json import GetVacancionJson


class UserInteractionHH(InputUserError):
    """
    Класс принимает от пользователя запрос и записывает результат в файл json
    """
    def user_request(self):
        query_user = self.user_input_str()
        top_n = self.user_input_int()
        info_vacancions = GetVacancionJson(query_user, top_n)
        info_vacancions.vacancion_json_write()


class UserInteractionJson(JsonUserError):
    """
    Класс принимает от пользователя запрос и выводит отсортированный список
    """
    def json_request(self):
        vacanciens_list = []
        json_vacant_file = VacancionsSort()
        vacancies_json = json_vacant_file.vacation_sorted()
        salary_from = self.user_input_int()
        city = self.user_input_str()
        for vacanc in vacancies_json:
            if salary_from > vacanc["salary_from"]:
                continue
            elif city == vacanc["city"] or city == "":
                vacanciens_list.append(vacanc)
        for conclusion in vacanciens_list:
            print(f"Дата: {conclusion['date']}\n"
                  f"Название вакансии: {conclusion['name_vacancion']}\n"
                  f"Город: {conclusion['city']}\n"
                  f"Заработная плата от: {conclusion['salary_from']}\n"
                  f"Требования: {conclusion['skill_t']}\n"
                  f"Ответственность: {conclusion['skill_o']}\n")
        if len(vacanciens_list) == 0:
            print('Результатов не найдено')

if __name__ == '__main__':
    v = UserInteractionJson()
    v.json_request()