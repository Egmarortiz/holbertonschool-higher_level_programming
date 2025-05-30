#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    seen = set()
    for item in my_list:
        if item not in seen:
            seen.add(item)
            total += item
    return total
