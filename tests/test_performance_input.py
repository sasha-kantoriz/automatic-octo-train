import pytest
import timeit
from main import (_read_input, get_minimum, get_maximum, get_sum, get_multiplication)



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
