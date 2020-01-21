#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding="UTF-8") as f:
        read_data = f.readlines()
        if (nb_lines <= 0 or nb_lines >= len(read_data)):
            for i in read_data:
                print(i, end="")
        else:
            for i in range(nb_lines):
                print("{}".format(read_data[i]), end="")
