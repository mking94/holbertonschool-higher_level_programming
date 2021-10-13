#!/usr/bin/python3
"""
Method append file
"""


def append_write(filename="", text=""):
    """ function that add text at the end of file
    """
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return myfile.write(text)
