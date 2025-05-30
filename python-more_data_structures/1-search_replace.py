#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for rep in my_list:
        if rep == search:
            search = replace
            new_list.append(rep)
        return new_list.append(rep)
