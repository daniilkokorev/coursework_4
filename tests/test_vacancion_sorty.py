import pytest
from src.vacancion_sorty import VacancionsSort


@pytest.fixture
def test_vacancie():
    return VacancionsSort()


def test_vacation_sorted_list(test_vacancie):
    # проверяем объекты класса
    assert test_vacancie.vacantion_sorty_list == []
    assert test_vacancie.date_formated == None


def test_vacation_sorted(test_vacancie):
    # проверяем метод вывода отсортированного списка
    assert test_vacancie.vacation_sorted() == [{'city': 'Москва',
                                          'date': '23.02.2024',
                                          'name_vacancion': 'Водитель персональный/водитель семейный',
                                          'salary_from': 110000,
                                          'salary_to': 110000,
                                          'skill_o': 'Составление оптимального маршрута движения с учетом дорожной '
                                                     'обстановки. Контроль за техническим состоянием и внешним видом '
                                                     'автомобиля. Полная конфиденциальность информации во...',
                                          'skill_t': 'Наличие водительского удостоверения категории В. Опыт работы от '
                                                     '5 лет ПЕРСОНАЛЬНЫМ <highlighttext>ВОДИТЕЛЕМ</highlighttext> '
                                                     'РУКОВОДИТЕЛЯ. Хорошее знание Москвы и Московской области и...'}]


def test_error_vacation_sorted():
    # проверяем на ошибку передачи данных
    with pytest.raises(TypeError):
        VacancionsSort("")
