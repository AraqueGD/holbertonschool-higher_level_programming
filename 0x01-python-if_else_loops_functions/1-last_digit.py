#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    digit = (number * -1 % 10) * -1
else:
    digit = number % 10
if (digit > 5):
    print("Last Digit of", number, "is {:d} and greater than 5".format(digit))
elif digit < 6 and digit != 0:
    print("Last Digit of", number, "is {:d} and is less than 6 and not 0"
          .format(digit))
else:
    print("Last Digit of", number, "is {:d} and is 0".format(digit))
