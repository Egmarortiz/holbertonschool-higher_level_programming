#!/usr/bin/python3
"""docustring"""


class Square:
    """docustring"""
    def __init__(self, size=0):
    """docustring"""
        self.__size = size
    @property
    def size(self):
    """docustring"""
        return self.__size
    @size.setter
    def size(self, value):
    """docustring"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
    """docustring"""
        return self.__size ** 2


