#!/usr/bin/python3
"""Module that defines a class Student with reload_from_json."""


class Student:
    """Represent a student defined by a first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the student's first name.
            last_name (str): the student's last name.
            age (int): the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student instance.

        Args:
            attrs (list): optional list of attribute names to include.
                If not a list, all attributes are returned.

        Returns:
            dict: the filtered or full dictionary representation.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): a dictionary mapping attribute names to values.
        """
        for key, value in json.items():
            setattr(self, key, value)
