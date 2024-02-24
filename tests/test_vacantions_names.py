import pytest
from src.vacantions_names import Vacancions


@pytest.fixture
def test_vacancie():
    return Vacancions("python", 1)


def test_str(test_vacancie):
    # тестируем метод str
    assert str(test_vacancie) == 'python'


def test_repr(test_vacancie):
    # тестируем метод repr
    assert repr(test_vacancie) == 'Vacancions(python, 1)'


def test_error_name(test_vacancie):
    with pytest.raises(AttributeError):
        test_vacancie.name_vacancion = 'src'


def test_error_page(test_vacancie):
    with pytest.raises(AttributeError):
        test_vacancie.page_vacancion = []
