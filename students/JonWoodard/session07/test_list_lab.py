#!/usr/bin/python
# import pytest  # used for the exception testing
from list_lab import fruit_2


def test_fruit_2():

    assert fruit_copy != master_fruit
    assert len(fruit_copy) == (len(master_fruit) - 1)
    for item in fruit_copy:
        assert item[::-1] in master_fruit
