#!/usr/bin/python3
"""Module that defines a class Student."""


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

    def to_json(self):
        """Return the dictionary representation of the Student instance."""
        return self.__dict__
