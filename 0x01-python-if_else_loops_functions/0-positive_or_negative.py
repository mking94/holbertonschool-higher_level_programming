#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    print(number,"is zero")
elif number < 0:
    print(number,"is negative")
else:
    print(number,"is positive")
