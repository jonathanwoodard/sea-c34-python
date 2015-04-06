"""
Write a function that returns a list of n functions, such that each 
one, when called, will return the input value, incremented by an 
increasing number.
Args:
    n: The number of functions to create.
Returns:
    Each function will return the input value, n, incremented by n.
"""

list_of_functions = []


def make_functions(n):
    def f(n):
        for i in range(n+1):
            list_of_functions.append(lambda i: i + n)
    print(list_of_functions)
