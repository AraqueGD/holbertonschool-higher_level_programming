#!/usr/bin/python3
def number_of_lines(filename=""):
    lineNum = 0
    with open(filename, 'r', encoding="UTF-8") as f:
        while f.readline():
            lineNum += 1
        return (lineNum)
