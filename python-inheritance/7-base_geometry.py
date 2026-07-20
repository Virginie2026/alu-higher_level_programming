#!/usr/bin/python3
"""Module that defines a class BaseGeometry with an integer validator."""


class BaseGeometry:
    """Represent a base geometry object."""

    def area(self):
        """Raise an exception since area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): the name of the attribute being validated.
            value: the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
