#!/usr/bin/python3
"""Module that defines a function to insert a line after a match."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a search string.

    Args:
        filename (str): the path of the file to modify.
        search_string (str): the string to search for in each line.
        new_string (str): the line to insert after a matching line.
    """
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
