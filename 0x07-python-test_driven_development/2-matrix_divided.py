#!/usr/bin/python3
""" Matrix Function Dived One Divisor """


def matrix_divided(matrix, div):

    """
        Parameter:
                - Matrix = A list the Int or FLoats
                - Div = Number Divisor
        Errors:
                - ZeroDivisorError = division by zero
                - TypeError = div must be a number
                - TypeError = The matrix must contain more than one element
                - TypeError = Each row of the matrix must have the same size
                - TypeError = matrix must be a matrix (list of lists) of intege
                            rs/floats
                RETURN = New List Elements Divided
    """
    new_list = []
    if (div is 0):
        raise ZeroDivisionError("division by zero")
    elif (type(div) is not float and type(div) is not int):
        raise TypeError("div must be a number")

    if(len(matrix) <= 1):
        raise TypeError("The matrix must contain more than one element")

    for a in matrix:
        if (len(a) != len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")

    for i in matrix:
        for x in i:
            if (type(x) is not int and type(x) is not float):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
    x = - 1
    for b in matrix:
        new_list.append([])
        x += 1
        for h in range(len(b)):
            new_list[x].append(round(b[h] / div, 2))
    return new_list
