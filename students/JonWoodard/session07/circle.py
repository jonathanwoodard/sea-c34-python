#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius
        self._diameter = self.radius * 2
        self._area = math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self._diameter

    @property
    def area(self):
        return self._area

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = self._diameter / 2

    def __str__(self):
        return u'Circle with radius: {:.6f}'.format(self.radius)

    def __repr__(self):
        return u'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius
