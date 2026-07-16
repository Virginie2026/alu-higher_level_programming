#!/usr/bin/python3
"""Module that defines a class Square with size validation."""


class Square:
    """Represent a square defined by a private, validated size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): the size of the new square (default 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
