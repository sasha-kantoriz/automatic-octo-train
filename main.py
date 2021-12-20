#!/usr/bin/python3

from functools import reduce



def memory_outage_handler(f):
    def catch_memory_outage(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except MemoryError as e:
            print('Input File Too Large. Aborting...')
            exit(1)
    return catch_memory_outage



@memory_outage_handler
def _read_input(file_path) -> list:
    numbers = list()
    with open(file_path) as fp:
        nums = fp.read().split()
        for num in nums:
            numbers.append(int(num))
    return numbers


@memory_outage_handler
def get_maximum(array) -> int:
    return max(array)


@memory_outage_handler
def get_minimum(array) -> int:
    return min(array)


@memory_outage_handler
def get_sum(array) -> int:
    return sum(array)


@memory_outage_handler
def get_multiplication(array) -> int:
    multiply = lambda x,y: x*y
    return reduce(multiply, array)
