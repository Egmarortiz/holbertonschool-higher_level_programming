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
        div (int/float): The divisor.

    Returns:
        list of list of float: A new matrix with the results of the division.

    Raises:
        TypeError: If the matrix is not a list of lists or if the elements
            are not integers or floats.
        ZeroDivisionError: If div is zero.
    """

    # 1. matrix must be list of lists
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        len(matrix) == 0):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")

    # 2. all rows must have same size
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # 3. all elements must be int or float
    for row in matrix:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError("matrix must be a matrix
                                (list of lists) of integers/floats")

    # 4. div must be number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 5. build and return new matrix
    new_matrix = []
    for row in matrix:
        new_row = [round(el / div, 2) for el in row]
        new_matrix.append(new_row)

    return new_matrix
    return matrix
