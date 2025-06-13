#!/usr/bin/python3
""" Module contains a simple square"""


class Square:
    """simple class"""
    def __init__(self, size):
        self.__size = size
    if not isinstance(size, (int, float)):
        raise TypeError("size must be a number")
    if size < 0:
        raise ValueError("size must be >= 0")