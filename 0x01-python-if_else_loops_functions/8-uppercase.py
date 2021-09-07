#!/usr/bin/python3
def uppercase(str):
    while str != "":
        if ord(str[0]) in range(97, 123):
            print("{:c}".format(ord(str[0])-32), end="")
        else:
            print(str[0], end="")
        str = str[1:]

