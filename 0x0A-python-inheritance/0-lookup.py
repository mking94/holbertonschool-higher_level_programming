"""Defines an object attribute lookup function."""

def lookup(obj):
    list = []
    for attributes in dir(obj):
        list.append(attributes)
    return list
