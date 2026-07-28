#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices (m_a and m_b).

    Args:
        m_a (list): First matrix (list of lists of integers/floats).
        m_b (list): Second matrix (list of lists of integers/floats).

    Returns:
        list: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b are not lists, list of lists,
                    contain non-numbers, or are not rectangular.
        ValueError: If m_a or m_b are empty or cannot be multiplied.
    """
    # 1. Validation: list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. Validation: list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. Validation: not empty ([] or [[]])
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. Validation: contain only integers or floats
    for row in m_a:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # 5. Validation: rectangular (all rows same size)
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 6. Validation: compatibility for multiplication
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication logic
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            row_result.append(total)
        result.append(row_result)

    return result
