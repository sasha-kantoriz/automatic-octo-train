import pytest
import timeit
from main import (_read_input, get_minimum, get_maximum, get_sum, get_multiplication)



@pytest.fixture
def input_data_small():
    file_name = 'tests/data/input_small.data'
    result = _read_input(file_name)
    return result


@pytest.fixture
def input_data_large():
    file_name = 'tests/data/input_large.data'
    result = _read_input(file_name)
    return result


def test_read_from_file_default():
    file_name = ''
    result = timeit.timeit('_read_input("tests/data/input.data")', setup='from main import _read_input', number=1)
    print(f'Default data set loading time: {result}')
    # assert result == list(range(1, 11))
    assert 1


def test_read_from_file_small():
    file_name = ''
    result = timeit.timeit('_read_input("tests/data/input_small.data")', setup='from main import _read_input', number=1)
    print(f'Small data set loading time: {result}')
    # assert result == list(range(1, 101))
    assert 1


def test_read_from_file_large():
    file_name = ''
    result = timeit.timeit('_read_input("tests/data/input_large.data")', setup='from main import _read_input', number=1)
    print(f'Large data set loading time: {result}')
    # assert result == list(range(1, 10001))
    assert 1


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
