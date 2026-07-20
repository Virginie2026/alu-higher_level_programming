#!/usr/bin/python3
"""Module that defines a function to safely add a new attribute."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object, if possible.

    Args:
        obj: the object to add an attribute to.
        name (str): the name of the new attribute.
        value: the value of the new attribute.

    Raises:
        TypeError: if the object can't have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
