#!/usr/bin/python3
"""Module defining the Square class with size getter and setter."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance using Rectangle constructor."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square (updates width and height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
