#!/usr/bin/python3
"""Module that defines a class Square inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, built on top of the Rectangle class."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the printable string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
