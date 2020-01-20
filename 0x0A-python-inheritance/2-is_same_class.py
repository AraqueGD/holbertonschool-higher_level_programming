#!/usr/bin/python3
"""Defines if object is exactly an instance of the specified class."""


def is_same_class(obj, a_class):
    """ Check if an object is an instance of a giving class.
    Args:
        obj: Object to check.
        a_class: It's the type of class to be compared

    Returns:
        True the obj is the same class of the a_class
        False if not is the same class type
    """
    return type(obj) == a_class
