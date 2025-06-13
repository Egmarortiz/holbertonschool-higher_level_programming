#!/usr/bin/python3
""" Module contains a simple square"""

class Square:
    """ Module contains a simple square"""
    def __init__(self, size=0):
        """ Module contains a simple square"""
        self.__size = size
        if not isinstance(size, int):
            """ Module contains a simple square"""
            raise TypeError("size must be an integer")
        if size < 0:
            """ Module contains a simple square"""
            raise ValueError("size must be >= 0")
