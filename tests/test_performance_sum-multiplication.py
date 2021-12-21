import timeit



def test_sum_default():
    result = timeit.timeit('get_sum(data)',
        setup='from main import _read_input, get_sum; data = _read_input("tests/data/input.data")',
        number=1
    )
    print(f'Default data set: calculating SUM value, time: {result}')


def test_sum_small():
    result = timeit.timeit('get_sum(data)',
        setup='from main import _read_input, get_sum; data = _read_input("tests/data/input_small.data")',
        number=1
    )
    print(f'Small data set: calculating SUM value, time: {result}')


def test_sum_large():
    result = timeit.timeit('get_sum(data)',
        setup='from main import _read_input, get_sum; data = _read_input("tests/data/input_large.data")',
        number=1
    )
    print(f'Large data set: calculating SUM value, time: {result}')


def test_multiplication_default():
    result = timeit.timeit('get_multiplication(data)',
        setup='from main import _read_input, get_multiplication; data = _read_input("tests/data/input.data")',
        number=1
    )
    print(f'Default data set: calculating MULTIPLICATION value, time: {result}')


def test_multiplication_small():
    result = timeit.timeit('get_multiplication(data)',
        setup='from main import _read_input, get_multiplication; data = _read_input("tests/data/input_small.data")',
        number=1
    )
    print(f'Small data set: calculating MULTIPLICATION value, time: {result}')


def test_multiplication_large():
    result = timeit.timeit('get_multiplication(data)',
        setup='from main import _read_input, get_multiplication; data = _read_input("tests/data/input_large.data")',
        number=1
    )
    print(f'Large data set: calculating MULTIPLICATION value, time: {result}')
