#!/usr/bin/python3
"""Module that defines a class Square that is printable."""


class Square:
    """Represent a square defined by a private size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): the size of the new square (default 0).
            position (tuple): the position of the square (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): the new size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): a tuple of 2 positive integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character '#', respecting position.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the string representation matching my_print output."""
        if self.__size == 0:
            return ""
        lines = ["\n" * self.__position[1] +
                 " " * self.__position[0] + "#" * self.__size]
        for _ in range(self.__size - 1):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
