#!/usr/bin/python
def safe_input():

    """
    This function will take raw user input and return 'None'
    rather than raising exceptions.
    """

    raw_input('Please input a value ->')
    try:
        return (raw_input())
    except:
        EOFError or KeyboardInterrupt
        return 'None'

