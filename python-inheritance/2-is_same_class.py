#!/usr/bin/python3
"""Module that defines a function to check exact class membership."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        bool: True if type(obj) is exactly a_class, False otherwise.
    """
    return type(obj) is a_class
