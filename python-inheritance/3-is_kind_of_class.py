#!/usr/bin/python3
"""Module that defines a function to check class membership by heritage."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or its subclasses.

    Args:
        obj: the object to check.
        a_class: the class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or any of its
            subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
