#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sq_mtx = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for integer in range(len(matrix)):
        for row in range(len(matrix[0])):
            sq_mtx[integer][row] = matrix[integer][row] ** 2

    return sq_mtx
