# submit 3 questions about lambdas and functional programming
def funct_1(n):
    """
    What does the map function do?
    """
    new_list = map(lambda x: x**2, range(n))
    print(new_list)

funct_1(10)


def funct_2(n):
    """
    How do you use a filter to get the desired values from a list/dict?
    """
    newer_list = filter((lambda x: (x**2) % 3 == 0), range(n))
    # I can only get this to return x, not x**2
    # There must be a way to do it in one line, but I'm not seeing it
    newest_list = [x**2 for x in newer_list]
    print(newest_list)

funct_2(50)


def funct_3(n):
    """
    Is there a difference between using map/filter/reduce or comprehensions?
    Is one preferred over the other?
    Is it context dependent?
    """
    old_list = [i**2 for i in range(n)]
    new_list = map(lambda x: x**2, range(n))
    print("{}\n{}".format(old_list, new_list))
    assert old_list == new_list

funct_3(10)
