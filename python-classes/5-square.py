#!/usr/bin/python3
"""Module 3-square: defines a Square."""


class Square:
    def __init__(self, size=0):
        """Module 3-square: defines a Square."""
        self.__size = size

    @property
    def size(self):
        """Module 3-square: defines a Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Module 3-square: defines a Square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Module 3-square: defines a Square."""
        return self.__size ** 2

    def my_print(self):
        """Module 3-square: defines a Square."""
        for square in range(size):
            print("{}".format("#" * size)
