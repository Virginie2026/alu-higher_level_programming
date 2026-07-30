#!/usr/bin/python3
"""Module defining the Square class inheriting from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance using Rectangle constructor."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
