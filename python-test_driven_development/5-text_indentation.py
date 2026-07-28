#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    There should be no space at the beginning or at the end
    of each printed line.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = True
    for char in text:
        if skip_space and char == ' ':
            continue
        skip_space = False
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n")
            skip_space = True
