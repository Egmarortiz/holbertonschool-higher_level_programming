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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """docustring"""
        return self.__size ** 2


