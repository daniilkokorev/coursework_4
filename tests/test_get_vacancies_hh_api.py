import pytest
from src.get_vacancies_hh_api import GetvacanciesHHAPI


@pytest.fixture
def test_vacancie():
    return GetvacanciesHHAPI("python", 1)


def test_url_hh(test_vacancie):
    # проверяем url
    assert test_vacancie.url_hh == 'https://api.hh.ru/'


def test_str(test_vacancie):
    # тестируем метод str
    assert str(test_vacancie) == 'python'


def test_repr(test_vacancie):
    # тестируем метод repr
    assert repr(test_vacancie) == 'GetvacanciesHHAPI(python, 1)'


def test_error_get_vacation():
    # тестируем ошибку ввода данных
    with pytest.raises(TypeError):
        GetvacanciesHHAPI()
