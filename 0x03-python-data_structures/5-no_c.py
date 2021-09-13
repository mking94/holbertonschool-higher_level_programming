#!/usr/bin/python3
def no_c(my_string):
    liste = []
    j = 0
    for i in range(0, len(ch)):
        if my_string[i] != 'c':
            liste.insert(j, my_string[i])
            j += 1
    return (''.join(liste))
