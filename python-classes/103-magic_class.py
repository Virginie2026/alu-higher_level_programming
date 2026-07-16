#!/usr/bin/python3
"""Module that defines MagicClass, reverse-engineered from bytecode."""
import math


class MagicClass:
    """Represent a circle defined by a private radius attribute."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius (int or float): the radius of the circle (default 0).

        Raises:
            TypeError: if radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
