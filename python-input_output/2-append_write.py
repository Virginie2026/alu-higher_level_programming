#!/usr/bin/python3
"""Module that defines a function to append text to a file."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF8 text file.

    Creates the file if it doesn't already exist.

    Args:
        filename (str): the path of the file to append to.
        text (str): the text to append.

    Returns:
        int: the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
