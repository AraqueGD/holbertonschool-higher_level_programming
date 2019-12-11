#!/usr/bin/python3
for idx in range(9):
    for idx2 in range(1, 10):
        if (idx2 < idx or idx2 == idx):
            continue
        if (idx != 8):
            print("{:d}{:d}".format(idx, idx2), end=', ')
        else:
            print("{:d}{:d}".format(idx, idx2))
