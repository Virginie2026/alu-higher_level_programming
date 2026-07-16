#!/usr/bin/python3
"""Module that defines a class Square with comparison operators."""


class Square:
    """Represent a square that can be compared to other squares by area."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int or float): the size of the new square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): the new size of the square.

        Raises:
            TypeError: if value is not a number.
            ValueError: if value is less than 0.
        """
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if this square's area equals another square's area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if this square's area differs from another's."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square's area is less than another's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square's area is <= another's."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square's area is greater than another's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square's area is >= another's."""
        return self.area() >= other.area()
