def exception_1():
    """
    Define one question about exceptions.
    Question 1:
        What kind of things will generate exceptions?
    """
    # try to do something that can't be done

    a = float(raw_input("Enter a number:\n-> "))
    b = float(raw_input("Enter another number:\n-> "))
    try:
        answer = a / b
    except:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not defined")
    print(answer)


def exception_2():
    """
    Define another question about exceptions.
    Question 2:
        How do you resolve an exception?
    """
    # use else to give it a way out of the exception
    a = float(raw_input("Enter a number:\n-> "))
    b = float(raw_input("Enter another number:\n-> "))
    try:
        answer = a / b
    except:
        if b == 0:
            print("Division by zero is not defined")
            b = float(raw_input("Enter another number:\n-> "))
            answer = a / b
    print(answer)
