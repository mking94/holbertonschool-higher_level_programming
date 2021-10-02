#!/usr/bin/python3
"""
function that adds two integers
"""


def add_integer(a, b=98):
    """
    handling errors before returning a + b
    """
    if isinstance(a, (int, float)) == False:
        raise TypeError('a must be an integer')
    if isinstance(b, (int, float)) == False:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
