#!/usr/bin/python3


class Square:
    """
    class Square with private instance attribute size
    """
    def __init__(self, size=0):
    """
    Initialize size
    """
        try:
            size += 1
            if (size - 1) < 0:
                raise ValueError()
            self.__size = size - 1
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
