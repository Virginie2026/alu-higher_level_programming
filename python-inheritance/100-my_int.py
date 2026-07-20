#!/usr/bin/python3
"""Module that defines a class MyInt with inverted == and != operators."""


class MyInt(int):
    """Represent an integer with == and != operators inverted."""

    def __eq__(self, value):
        """Return True if self and value are NOT equal (inverted)."""
        return int(self) != value

    def __ne__(self, value):
        """Return True if self and value ARE equal (inverted)."""
        return int(self) == value
