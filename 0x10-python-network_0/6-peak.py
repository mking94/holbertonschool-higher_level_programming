#!/usr/bin/python3
""" Function that return the peak in a list of integer"""
def find_peak(list_of_integers):
    y = list_of_integers[0]
    for x in list_of_integers:
        if x > y :
            y = x
    return y
