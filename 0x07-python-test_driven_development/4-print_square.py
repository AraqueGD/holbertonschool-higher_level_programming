#!/usr/bin/python3
""" Function Print Square """


def print_square(size):
    """
        Function Print Square and
        Erros Function
    """
    if (type(size) is not int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    elif (size < 0 and type(size) is float):
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size, end="")
        print()
