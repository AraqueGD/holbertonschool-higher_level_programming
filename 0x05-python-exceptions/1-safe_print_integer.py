#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value is int
        print("{:d}".format(value))
    except ValueError:
        return False
    finally:
        return True
