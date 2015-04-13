# submit 3 questions about comprehensions
def comp_1(n):
    """
    How do you create a new list using a list comprehension?
    """
    new_list = [i**2 for i in range(n)]
    print(new_list)
    print(len(new_list))
comp_1(10)


def comp_2(n):
    """
    How do you include loops and conditionals in a comprehension?
    """
    newer_list = [i**2 for i in range(n) if i**2 % 3 == 0]
    print(newer_list)
    print(len(newer_list))
comp_2(50)


def comp_3(n):
    """
    How do you create a dictionary with a comprehension?
    """
    new_dict = {i: i**2 for i in range(n) if i**2 % 3 == 0}
    print(new_dict)
    print(len(new_dict))
comp_3(50)
