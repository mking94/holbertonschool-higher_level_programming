"""Defines an object attribute lookup function."""

def lookup(obj):
    liste = []
    for attributes in dir(obj):
        liste.append(attributes)
    return liste
