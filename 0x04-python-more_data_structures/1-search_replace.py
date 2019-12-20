#!/usr/bin/python3
def func(x, search, replace):
    if x == search:
        return replace
    else:
        return x


def search_replace(my_list, search, replace):
    search = [search] * len(my_list)
    replace = [replace] * len(my_list)
    newList = list(map(func, my_list, search, replace))
    return newList
