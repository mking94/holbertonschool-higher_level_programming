#!/usr/bin/python3
""" Import Square Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class"""

    def __init__(self, size):
        """
        Constructor
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """prints the Square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
