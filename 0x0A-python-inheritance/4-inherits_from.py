#!/usr/bin/python3
""" Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """function to verify subclass"""
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    else:
        return False
