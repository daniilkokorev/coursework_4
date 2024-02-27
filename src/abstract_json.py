from abc import ABC, abstractmethod


class AbstractJson(ABC):
    """
    Абстрактный класс для работы с файлом
    """

    @abstractmethod
    def vacancion_json_write(self):
        pass

    @abstractmethod
    def vacancion_json_append(self):
        pass

    @abstractmethod
    def vacancion_json_clear(self):
        pass
