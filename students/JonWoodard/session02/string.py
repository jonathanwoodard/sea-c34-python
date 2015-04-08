# create module string.py
def string1():
    """
    Things about strings.
    """
    # put some code here
    a = "some random text"
    b = []
    if len(a) > 7:
        b.append(a[2:5])
    return b


def string2():
    """
    More things about strings.
    """
    # put some more code here
    another_string = "oh, boy, how about some more random text"
    print(another_string)
    print(another_string.replace(" random", ""))


def string3():
    """
    All you ever wanted to know about strings.
    """
    # another block of code here
    one_final_string = "this string has"
    one_final_string_part_2 = " even more text"
    print(one_final_string + one_final_string_part_2)
