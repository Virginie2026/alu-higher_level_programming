#!/usr/bin/python3
"""Module that defines a class Square with a private size attribute."""


class Square:
    """Represent a square defined by a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the new square.
        """
        self.__size = size
