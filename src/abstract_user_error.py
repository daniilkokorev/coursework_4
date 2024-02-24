from abc import ABC, abstractmethod


class UserError(ABC):
    """
    Класс для проверок ошибок
    """
    @abstractmethod
    def user_input_int(self):
        pass

    @abstractmethod
    def user_input_str(self):
        pass
