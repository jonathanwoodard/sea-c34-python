"""
Ask one question about classes in python
"""


def farm_animal(object):
    """
    One question:
    How do you create a new class?
    """
    def __init__(self, name, sound):
        """Initialize the class."""
        self.name = name
        self.sound = sound

    def basic_info(self):
        """Return the name and sound of the farm_animal."""
        print("The {name} says {sound}.".format(self.name, self.sound))
