#!/usr/bin/python
# import pytest  # used for the exception testing
from series import fibonacci
from series import lucas


def test_fib():

    assert fibonacci(2) == 1
    assert fibonacci(7) == 8
    assert fibonacci(27) == 121393


def test_luc():

    assert lucas(2) == 1
    assert lucas(7) == 18
    assert lucas(27) == 271443
