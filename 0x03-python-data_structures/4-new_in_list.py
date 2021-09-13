#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    b = []
    for i in range(len(my_list)):
        b.insert(i,my_list[i])
    if(idx < 0):
        return (my_list)
    elif(idx > len(my_list)):
        return (my_list)
    else:
        b[idx] = element
        return (b)
