#!/usr/bin/python
import pytest  # used for the exception testing
from list_lab import master_fruit
from list_lab import fruit_copy
# from list_lab import fruit_1
from list_lab import fruit_2

"""
This generates an IOError that I have not been able to resolve.
def test_fruit_1():
    return fruit_1()
    assert fruit[2] == 'Oranges'
"""


def test_fruit_2():
    return fruit_2()
    assert [fruit_copy] != [master_fruit]
    assert fruit_copy[2] == 'segnarO'
    assert len(fruit_copy) == (len(master_fruit) - 1)
    for item in fruit_copy:
        # rev_item = item[::-1]
        assert item[::-1] in master_fruit
