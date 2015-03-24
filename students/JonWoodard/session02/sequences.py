# create module sequences.py
def strings_as_sequences(string1, string2):
    """
    This function will explore the sequence properies of strings.
        Args:
            string1: a bunch of text to play with.
            string2: some more text.
        Return:
            information about the strings.
    """

    string1 = "I will not buy this record, it is scratched"
    string2 = "My hovercraft is full of eels"
    print(len(string1))
    print(len(string2))
    print((len(string1) - len(string2))**2)
    if "eels" in string2:
        print(string1[17:22])
    else:
        print(string1 + string2)


def lists_as_sequences(list1, list2):
    """
    This function will manipulate some lists.
        Args:
            list1: some animals.
            list2: some foods.
        Return:
            information from the lists.
    """

    list1 = []
    list2 = []
    list1.append["gorilla", "armadillo", "squid"]
    if "gorilla" in list1:
        list2.append["bananas"]
    if "penguin" not in list2:
        list1.append["penguin"]
        list1.remove["squid"]
    list1.sort
    list1[2] = "crocodile"
    print(list1)


def tuples_as_sequences(t):
    """
    This function will do some stuff with tuples.
    """
    t = 3, 1, 4, 3.14
    print(t)

