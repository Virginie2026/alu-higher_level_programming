#!/usr/bin/python3
"""This module defines the Square class, inheriting from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square, built on top of the Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.
            x (int): the horizontal offset of the square.
            y (int): the vertical offset of the square.
            id (int, optional): the id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (maps to both width and
        height).
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the square's attributes.

        Args:
            *args: new attribute values in the order id, size, x, y.
            **kwargs: new attribute values as key/value pairs, used
                only if *args is empty.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
