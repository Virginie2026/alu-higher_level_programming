#!/usr/bin/python3
"""Module that defines a function to convert an object to a dict."""


def class_to_json(obj):
    """Return the dictionary description of an object for serialization.

    Args:
        obj: an instance of a class with serializable attributes.

    Returns:
        dict: the dictionary representation of obj's attributes.
    """
    return obj.__dict__
