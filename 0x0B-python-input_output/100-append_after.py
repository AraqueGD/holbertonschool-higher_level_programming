#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    string = ""
    with open(filename, 'r+', encoding="utf-8") as f:
        for line in f:
            string += line
            if search_string in line:
                string += new_string
        f.write(string)
