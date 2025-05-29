#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    new_list = []

    for div in my_list:
        if div % 2 == 0:
            return new_list.append(True)
        else:
            return new_list.append(False)
