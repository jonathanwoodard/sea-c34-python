#!/usr/bin/python
# import pytest  # used for the exception testing
from _lambda import list_of_functions
# import __builtin__
# __builtin__.raw_input()

from _lambda import make_functions


def test_lambda():
    return 4
    # return 5
    assert list_of_functions[0](2) == 2
    assert list_of_functions[1](2) == 3
    assert list_of_functions[0](5) == 5
    assert list_of_functions[1](5) == 6
    assert list_of_functions[2](5) == 7
    assert list_of_functions[3](5) == 8
