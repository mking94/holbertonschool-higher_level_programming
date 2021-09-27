#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value += 1
        print("{:d}".format(value - 1))
        return(bool(1))
    except BaseException:
        return(bool(0))
