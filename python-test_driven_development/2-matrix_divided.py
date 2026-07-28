#!/usr/bin/python3
"""
This module contains the function matrix_divided, which divides all elements
of a matrix of numbers by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix: List of lists containing integers or floats.
        div: Number (integer or float) to divide the matrix elements by.

    Returns:
        A new matrix with the results of the division.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   if rows are not all the same size,
                   or if div is not an int or float.
        ZeroDivisionError: If div is equal to 0.
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg_type)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
