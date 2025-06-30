#!/usr/bin/python3

"""does it inherit"""


def inherits_from(obj, a_class):
    """does it inherit"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
