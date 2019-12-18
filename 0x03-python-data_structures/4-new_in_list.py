#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if (idx < 0):
        return (my_list)
    elif (idx > len(new_list) - 1):
        return (my_list)
    new_list.remove(new_list[idx])
    new_list.insert(idx, element)
    return (new_list)
