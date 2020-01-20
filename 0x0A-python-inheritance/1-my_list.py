#!/usr/bin/python3
""" Define an inherited list class my list. """


class MyList(list):
    """ Function Print Sorted List """

    def print_sorted(self):
        print(sorted(self))
