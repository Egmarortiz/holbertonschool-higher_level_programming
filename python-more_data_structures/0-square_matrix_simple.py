#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        for i, item in enumerate(row):
            new_matrix.append(item ** 2)
    return new_matrix
    return matrix



