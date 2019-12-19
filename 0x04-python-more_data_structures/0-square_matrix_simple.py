#!/usr/bin/python3
def square(lista):
    return(list(map(lambda x: x**2, lista)))
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(square, matrix))
    return(new_matrix)
