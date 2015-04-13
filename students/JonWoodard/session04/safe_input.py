#!/usr/bin/python
def safe_input(usr_in=None):

    """
    This function will take raw user input and return 'None'
    rather than raising exceptions.
    """

    try:
        usr_in = raw_input('Please input a value:\n -> ')
        return usr_in
    except (EOFError, KeyboardInterrupt):
        return 'None'

safe_input()
