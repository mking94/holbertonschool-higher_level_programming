#!/usr/bin/python3
def uppercase(str):
    ch = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            ch += chr(ord(c) - 32)
        else:
            ch += c
    print("{}".format(ch))
