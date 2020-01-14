#!/usr/bin/python3
""" Function Separate Text """


def text_indentation(text):

    """
        The Function Separate Text If Find ".?:"
        and Errors
    """
    sw = False
    if (type(text) is not str):
        raise TypeError("text must be a string")
    for i in text:
        if(i in ".?:"):
            print(i, end="")
            print("\n")
            sw = True
        else:
            if(sw == True):
                sw = False
                continue
            print(i, end="")
