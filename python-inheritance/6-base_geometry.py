#!/usr/bin/python3
"""Module that defines a class BaseGeometry with an area method."""


class BaseGeometry:
    """Represent a base geometry object."""

    def area(self):
        """Raise an exception since area is not implemented here."""
        raise Exception("area() is not implemented")
