def exception_1(quest1):
    """
    Define one question about exceptions.
    Question 1:
        What kind of things will generate exceptions?
    """
    # try to do something that can't be done

    a = int(raw_input)
    b = int(raw_input)
    answer = a / b
    if b == 0:
        raise ZeroDivisionError("Division by zero is not defined")


def exception_2(quest2):
    """
    Define another question about exceptions.
    Question 2:
        How do you resolve an exception?
    """
    # use else to give it a way out of the exception

    
