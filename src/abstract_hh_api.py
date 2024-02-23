from abc import ABC, abstractmethod


class AbstractHHAPI(ABC):
    """ Абстрактный класс для получения API с HeadHunter"""
    @abstractmethod
    def get_vacancies_hh_api(self):
        pass

    @abstractmethod
    def write_vacancions_list(self):
        pass
