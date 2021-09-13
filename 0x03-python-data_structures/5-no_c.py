#!/usr/bin/python3
def no_c(my_string):
    liste = []
    j = 0
    i = 0
    while i < len(my_string):
        if my_string[i] == 'c' or my_string[i] == 'C':
            i += 1
        else:
            liste.insert(j, my_string[i])
            j += 1
            i += 1
    return (''.join(liste))
