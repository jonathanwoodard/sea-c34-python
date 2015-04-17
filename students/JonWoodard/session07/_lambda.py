"""
Write a function that returns a list of n functions, such that each
one, when called, will return the input value, incremented by an
increasing number.
Args:
    n: The number of functions to create.
    a: The input value for the functions. This could be any numerical
        value, though here it is restricted to integers.
Returns:
    Each function will return the input value, a, incremented by n.
"""

list_of_functions = []


def make_functions(*args):
    """
    having the raw_input parameter in the function arguments
    raises 'IOError: reading from stdin while output is captured'
    in pytest. I have not figured out how to get around this yet,
    so I have temorarily removed the raw_input.
    ###(n=int(raw_input(u"Enter an integer:\n-> "))):###
    """
    n = 4
    for i in range(n):
        list_of_functions.append(lambda x, y=i: x + y)


# some tests

if __name__ == "__main__":
    make_functions()
    a = (int(raw_input(u"Enter another integer:\n-> ")))
    # this number will be the input for the functions created above,
    # and can be any integer.
    for i in range(len(list_of_functions)):
        print(list_of_functions[i](a))
        assert list_of_functions[i](a) == (i + a)

