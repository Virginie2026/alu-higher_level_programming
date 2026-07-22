#!/usr/bin/python3
"""Module that defines a function to write text to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file, creating or overwriting it.

    Args:
        filename (str): the path of the file to write to.
        text (str): the text to write.

    Returns:
        int: the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
