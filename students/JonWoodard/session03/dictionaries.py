def dictionary_1():
    """
    Define four questions about dictionaries and sets.
    Quesstion 1:
        How do you add things to a dictionary?
    """
    zoo_animals = ["lions", "tigers", "monkeys"]
    how_many = [3, 2, 11]
    in_the_zoo = {}

    in_the_zoo = dict(zip(zoo_animals, how_many))   
    print(in_the_zoo)

    in_the_zoo.update({"lemurs": 14})
    print(in_the_zoo)

    in_the_zoo.update([("sloths", 2), ])
    print(in_the_zoo)


def dictionary_2(quest2):
    """
    Define another question.
    Question 2:
        What types of things can be put in a dictionary?
    """
    in_the_zoo = {}
    in_the_zoo.update({"unicorns": 3.14})


def dictionary_3(quest3):
    """
    Define another question.
    Question 3:
        How do you access the items in a dictionary?
    """
    in_the_zoo = {"lions":3, "tigers": 2, "monkeys": 11, "lemurs": 14}
    in_the_zoo["lions"]
    in_the_zoo.get("lemurs")


def dictionary_4(quest4):
    """
    Define a last question.
    Question 4:
        How do you remove things from a dictionary?
    """

