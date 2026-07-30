#!/usr/bin/python3
"""This module defines the Base class for all other classes in the
project.
"""
import json
import csv


class Base:
    """Base class that manages the id attribute for all future classes
    and handles serialization/deserialization to/from JSON and CSV.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int, optional): the id of the instance. If None, an
                id is automatically assigned by incrementing the
                class-level object counter.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries (list): a list of dictionaries.

        Returns:
            str: the JSON string representation, or "[]" if the list
                is None or empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of a list of objects
        to a file.

        Args:
            list_objs (list): a list of instances that inherit from
                Base.
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries represented by a JSON string.

        Args:
            json_string (str): a JSON string representing a list of
                dictionaries.

        Returns:
            list: the list of dictionaries, or an empty list if
                json_string is None or empty.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance built from a dictionary of attributes.

        Args:
            **dictionary: key/value pairs of attributes to set.

        Returns:
            An instance of cls with all attributes set from
                dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file named
        <cls.__name__>.json.

        Returns:
            list: a list of instances, or an empty list if the file
                doesn't exist.
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write a list of objects to a CSV file named
        <cls.__name__>.csv.

        Args:
            list_objs (list): a list of instances that inherit from
                Base.
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
                return
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from a CSV file named
        <cls.__name__>.csv.

        Returns:
            list: a list of instances, or an empty list if the file
                doesn't exist.
        """
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=fieldnames)
                list_dicts = [
                    {k: int(v) for k, v in d.items()} for d in reader
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
