#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value += 1
        print("{}".format(value - 1))
    except BaseException:
        print("{} is not an integer".format(value))
