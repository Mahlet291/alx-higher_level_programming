#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        z = [x**2 for x in matrix[i]]
        new_matrix.append(z)
    return new_matrix
