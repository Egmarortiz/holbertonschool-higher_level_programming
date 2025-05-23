#!/usr/bin/python3

# 12 - FizzBuzz

def fizzbuzz():
    for num in range(101): 
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
