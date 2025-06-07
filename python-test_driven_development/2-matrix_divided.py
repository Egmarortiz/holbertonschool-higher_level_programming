#!/usr/bin/python3
"""
matrix_divided.py

Defines matrix_divided(matrix, div) that:
- Validates matrix is a list of lists of int/float, all rows same size
- Validates div is a non-zero int or float
- Returns a new matrix where each element is rounded(el / div, 2)
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of list of int/float): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of list of float: A new matrix with division results.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
            or if rows are not the same size, or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not matrix or any(
            not isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size"
        )

    for row in matrix:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(el / div, 2) for el in row]
        new_matrix.append(new_row)

    return new_matrix
    return matrix
