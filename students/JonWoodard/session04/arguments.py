# submit 3 questions about arguments
def arg_1(opt=2):
    """
    How do you define an optional argument?
    """
    result = 5 ** opt
    print(result)

arg_1()
arg_1(3)


def arg_2(**answer):
    """
    What is an example of a function using kwargs?
    """
    answer = (raw_input(u"What do you want to eat?\n-> "))
    print("{}".format(answer))

arg_2()


def arg_3(*enthusiasm, **answer):
    """
    What is an example of a function using both args and kwargs?
    """
    answer = (raw_input(u"What do you want to eat?\n-> "))
    enthusiasm = int(raw_input(
        u"How much do you want?\n"
        u"(This must be an integer)\n -> ")
        )
    print("{}!".format(enthusiasm * answer))

arg_3()
