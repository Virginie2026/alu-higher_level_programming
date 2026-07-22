#!/usr/bin/python3
"""Module that defines a function to build Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of size n.

    Args:
        n (int): the number of rows of the triangle.

    Returns:
        list: a list of lists of integers, or an empty list if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1] + [prev[j] + prev[j + 1] for j in range(len(prev) - 1)]
        row.append(1)
        triangle.append(row)
    return triangle
