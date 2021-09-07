#!/usr/bin/python3
i = 122
while i >= 97:
    print("{:c}{:c}".format(i,  i - 33),  end="")
    i -= 2
