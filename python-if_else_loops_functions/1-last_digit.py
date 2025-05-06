#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last = number % 10 if number >= 0 else number % -10

if last == 0:
    msg = "and is 0"
elif last < 6:
    msg = "and is less than 6 and not 0"
else:
    msg = "and is greater than 5"

print(f"Last digit of {number} is {last} {msg}")
