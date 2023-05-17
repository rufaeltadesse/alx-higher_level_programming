#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = matrix.copy()
    for j in range(len(matrix)):
        newmatrix[j] = list(map(lambda x: x * x, matrix[j]))
    return newmatrix
