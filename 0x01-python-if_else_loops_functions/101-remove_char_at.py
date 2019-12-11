#!/usr/bin/python3
def remove_char_at(str, n):
    if (n >= 0):
        change = str[:n] + str[n + 1:]
    else:
        change = str
    return (change)
