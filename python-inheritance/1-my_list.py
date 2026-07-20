#!/usr/bin/python3
"""Module that defines a class MyList inheriting from list."""


class MyList(list):
    """Represent a list that can print itself in sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
