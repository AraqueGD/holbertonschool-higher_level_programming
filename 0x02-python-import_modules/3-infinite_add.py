#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv) - 1
    suma = 0
    for i in range(argc):
        suma = suma + int(sys.argv[i + 1])

    print(suma)
