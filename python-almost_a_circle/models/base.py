#!/usr/bin/python3
"""
This module defines the Base class for managing unique ID attributes.
"""


class Base:
    """
    Base class to handle unique ID generation for instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int, optional): Custom ID for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
