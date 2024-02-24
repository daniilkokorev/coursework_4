from src.abstract_user_error import UserError


class InputUserError(UserError):
    """
    Класс отлавливает ошибки ввода пользователя
    """
    query_user = None
    top_n = None

    def user_input_int(self) -> int:
        """
        проверяем правильность ввода количества вакансий
        """
        self.top_n = input("Введите количество вакансий для вывода в топ N: ")
        if self.top_n.isalpha():
            raise ValueError("Количество должно быть числом")
        elif self.top_n == "":
            raise AttributeError("Количество не может быть пустым")
        elif int(self.top_n) <= 0:
            raise TypeError("Количество должно быть положительным числом")
        elif int(self.top_n) > 100:
            self.top_n = 100
        return int(self.top_n)

    def user_input_str(self) -> str:
        """
        Отлавливвввваем ошибки при вводе запроса вакансии
        """
        self.query_user = input("Введите поисковый запрос: ")
        if self.query_user == "":
            raise ValueError("Введите название вакансии")
        elif self.query_user.isdigit():
            raise TypeError("Не может быть числом")
        return self.query_user
