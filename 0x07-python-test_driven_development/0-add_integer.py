#!/usr/bin/python3

""" Program addition two integer. """


def add_integer(a, b=98):

    """
        Function Add Integers
        and Errors.
    """

    if (isinstance(a, float) or isinstance(b, float)):
        a = int(a)
        b = int(b)
    elif (type(a) is not int):
        raise TypeError("a must be an integer")
    elif (type(b) is not int):
        raise TypeError("b must be an integer")
    return a + b
