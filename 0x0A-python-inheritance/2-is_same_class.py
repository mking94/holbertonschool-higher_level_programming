#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
