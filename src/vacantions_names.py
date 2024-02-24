class Vacancions:
    """
    Класс для инкапсуляции названия и количества вакансий
    """

    def __init__(self, name_vacancion, page_vacancion):
        self.__name_vacancion = name_vacancion
        self.__page_vacancion = page_vacancion

    @property
    def name_vacancion(self):
        return self.__name_vacancion

    @property
    def page_vacancion(self):
        return self.__page_vacancion

    def __str__(self):
        return f"{self.__name_vacancion}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name_vacancion}, {self.__page_vacancion})"
