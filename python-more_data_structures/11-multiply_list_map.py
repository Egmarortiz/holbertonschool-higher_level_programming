#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    mult = map(lambda x: x * number, my_list)
    multiplied = list(mult)
    return multiplied
