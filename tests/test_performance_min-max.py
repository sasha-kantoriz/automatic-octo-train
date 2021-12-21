import timeit



def test_minimum_default():
    result = timeit.timeit('get_minimum(data)',
        setup='from main import _read_input, get_minimum; data = _read_input("tests/data/input.data")',
        number=1
    )
    print(f'Default data set selecting MIN value, time: {result}')


def test_minimum_small():
    result = timeit.timeit('get_minimum(data)',
        setup='from main import _read_input, get_minimum; data = _read_input("tests/data/input_small.data")',
        number=1
    )
    print(f'Small data set selecting MIN value, time: {result}')


def test_minimum_large():
    result = timeit.timeit('get_minimum(data)',
        setup='from main import _read_input, get_minimum; data = _read_input("tests/data/input_large.data")',
        number=1
    )
    print(f'Large data set selecting MIN value, time: {result}')


def test_maximum_default():
    result = timeit.timeit('get_maximum(data)',
        setup='from main import _read_input, get_maximum; data = _read_input("tests/data/input.data")',
        number=1
    )
    print(f'Default data set selecting MAX value, time: {result}')


def test_maximum_small():
    result = timeit.timeit('get_maximum(data)',
        setup='from main import _read_input, get_maximum; data = _read_input("tests/data/input_small.data")',
        number=1
    )
    print(f'Small data set selecting MAX value, time: {result}')


def test_maximum_large():
    result = timeit.timeit('get_maximum(data)',
        setup='from main import _read_input, get_maximum; data = _read_input("tests/data/input_large.data")',
        number=1
    )
    print(f'Large data set selecting MAX value, time: {result}')
