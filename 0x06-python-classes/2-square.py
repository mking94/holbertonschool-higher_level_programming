#!/usr/bin/python3
class Square:
    __size
    def __init__(self, size=0):
        try:
            size += 1
            if (size - 1) < 0:
                raise ValueError()
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
