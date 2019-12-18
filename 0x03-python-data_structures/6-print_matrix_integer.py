#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(''.join([' '.join(['{}'.format(item) for item in row])]))
