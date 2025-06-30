#!/usr/bin/python3
"""Defining a square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        """Initialize parameters"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate area"""
        return self.__size ** 2
