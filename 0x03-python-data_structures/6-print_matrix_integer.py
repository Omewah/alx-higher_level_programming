#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for integer in range(len(matrix)):
        for row in range(len(matrix[integer])):
            if row != 0:
                print(" ", end='')
            print("{:d}".format(matrix[integer][row]), end='')
        print()
