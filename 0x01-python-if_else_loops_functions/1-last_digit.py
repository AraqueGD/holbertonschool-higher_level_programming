#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10 if number > 0 else number % -10
if (digit > 5):
    print("Last Digit of", number, "is {} and greater than 5".format(digit))
elif digit == 0:
    print("Last Digit of", number, "is {} and is 0".format(digit))
else:
    print("Last Digit of", number, "is {} and is less than 6 and not 0".format(digit))
