#!/usr/bin/python3

def max_integer(my_list=[]):
    max_val = my_list[0]  # Start by assuming the first item is the largest
    for num in my_list:
        if num > max_val:
            max_val = num  # Update max_val if a bigger number is found
    return max_val
