#!/usr/bin/python3
"""Module that defines a class Rectangle inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle, validated via BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.

        Raises:
            TypeError: if width or height is not an integer.
            ValueError: if width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the current area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the printable string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
