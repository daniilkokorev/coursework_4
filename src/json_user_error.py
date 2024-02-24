from src.abstract_user_error import UserError


class JsonUserError(UserError):
    """
    Класс отлавливает ошибки при чтении файла json
    """
    salary_from = None
    city = None

    def user_input_int(self):
        # проверяем правильность ввода зарплаты
        self.salary_from = input("Введите желаемую зарплату: ")
        if self.salary_from.isalpha():
            raise ValueError("Зарплата должна быть числом")
        if self.salary_from == "":
            self.salary_from = 0
        if int(self.salary_from) < 0:
            raise TypeError("Зарплата должна быть положительным числом")
        return int(self.salary_from)

    def user_input_str(self):
        # проверяет правильность ввода названия города
        self.city = input("Введите название города: ").title()
        if self.city.isdigit():
            raise TypeError("Не может быть числом")
        return self.city
