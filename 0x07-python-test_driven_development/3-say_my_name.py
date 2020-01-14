#!/usr/bin/python3
""" Function Print My Full Name """


def say_my_name(first_name, last_name=""):
    """
        Function Prints Names and Last Name
        and Erros
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    elif (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    return (print("My Name is {} {}".format(first_name, last_name)))
