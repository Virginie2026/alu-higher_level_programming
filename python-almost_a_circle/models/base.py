#!/usr/bin/python3
"""Module defining the Base class with JSON string conversion."""
import json


class Base:
    """Base class for managing id attribute in all classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with id management."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
