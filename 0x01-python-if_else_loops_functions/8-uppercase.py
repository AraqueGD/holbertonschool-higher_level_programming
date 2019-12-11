#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        tmp = ord(str[i])
        if (tmp >= 97 and tmp <= 122):
            tmp -= 32
        print("{}".format(chr(tmp)), end="")
    print()
