# create module iteration.py
def loop1(n):
    """
    Iterate something over and over.
        Args:
            n: number of iterations
        Return:
            the result of performing a task n times
    """
    for i in range(4):
        return n**i

def loop2(a, b):
    """
    Iterate over and over.
        Args:
            a: the thing to be iterated
            b: the number of iterations
        Return:
            a iterated b times.
    """
    a = "some_string"
    b = len(a)
    while b < 100:
        a = a * b % 2
    print(len(a))


def loop3(c):
    """
    More iterations. Insert a break if things get out of control.
    """
    c = 2. / 3.
    d = (c,)
    if len(d) > 50:
        break
