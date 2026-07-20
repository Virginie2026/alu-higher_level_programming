#!/usr/bin/python3
"""Module that defines a function to check indirect class inheritance."""


def inherits_from(obj, a_class):
    """Check if an object's class inherited from the specified class.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        bool: True if obj is an instance of a class that inherited
            (directly or indirectly) from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
