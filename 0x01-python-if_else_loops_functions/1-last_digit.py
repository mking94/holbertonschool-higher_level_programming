#!/usr/bin/python3
import random
number = random.randint(-10000,10000)
x = 1
if number < 0:
    x = -1
if abs(number) % 10 == 0:
    print("Last digit of",number,"is",(abs(number)%10)*x,"and is 0")
elif abs(number) % 10 in range(7):
    print("Last digit of",number,"is",(abs(number)%10)*x,"and is less the 6 and not 0")
else:
    print("Last digit of",number,"is",(abs(number)%10)*x,"and is greater then 5")