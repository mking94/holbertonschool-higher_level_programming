#!/usr/bin/python3
"""
Method write file
"""


def write_file(filename="", text=""):
    """
write into file
"""
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return myfile.write(text)
