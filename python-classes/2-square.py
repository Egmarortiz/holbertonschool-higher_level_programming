#!/usr/bin/python3
""" Module contains a simple square"""

class Square:
    def __inti__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be >= 0")
