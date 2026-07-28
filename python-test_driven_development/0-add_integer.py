#!/usr/bin/python3
"""
This module provides a function for adding two numbers.
It accepts integers and floats, converts floats to integers,
and returns the sum as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Floats are casted to integers before addition.

    Args:
        a: First number (int or float).
        b: Second number (int or float, default is 98).

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
