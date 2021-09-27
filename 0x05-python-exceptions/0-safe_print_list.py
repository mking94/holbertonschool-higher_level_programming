#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print((' '.join(map(str, my_list[0:x]))).replace(" ", ""))
        return(x)
    except BaseException:
        print("Index outside of length")
