#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        return bool(1)
    else:
        return bool(0)
def uppercase(str):
    while str != "":
        if islower(str[0]):
            print("{:c}".format(ord(str[0])-32), end="")
        else:
            print(str[0], end="")
        str = str[1:]
