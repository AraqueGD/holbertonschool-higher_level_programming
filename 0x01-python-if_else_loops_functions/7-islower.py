#!/usr/bin/env python3
def islower(c):
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in a:
        if (ord(c) == ord(i)):
            return True
        else:
            continue
        return False
