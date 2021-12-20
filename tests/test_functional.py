import pytest
from main import (_read_input, get_minimum, get_maximum, get_sum, get_multiplication)



def test_read_from_file():
    file_name = 'tests/data/input.data'
    result = _read_input(file_name)
    assert result == [10,9,8,7,6,5,4,3,2,1]


@pytest.fixture
def input_data_default():
    file_name = 'tests/data/input.data'
    result = _read_input(file_name)
    return result


def test_minimum(input_data_default):
    result = get_minimum(input_data_default)
    assert result == 1


def test_maximum(input_data_default):
    result = get_maximum(input_data_default)
    assert result == 10


def test_sum(input_data_default):
    result = get_sum(input_data_default)
    assert result == 55


def test_multiplication(input_data_default):
    result = get_multiplication(input_data_default)
    assert result == 3628800
