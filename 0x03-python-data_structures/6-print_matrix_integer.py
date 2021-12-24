#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = len(matrix)
    for i in range(x):
        for j in range(len(matrix[i])):
            if j < len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]), end="")
        print()
