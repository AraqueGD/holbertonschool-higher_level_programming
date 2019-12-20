#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    for key, valor in new.items():
        if (valor == value):
            del a_dictionary[key]
    return(a_dictionary)
