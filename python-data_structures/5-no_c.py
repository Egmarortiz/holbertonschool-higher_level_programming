#!/usr/bin/python3

def no_c(my_string):
    filtered = [x for x in my_string if x not in ('c', 'C')]
    return "".join(filtered)
