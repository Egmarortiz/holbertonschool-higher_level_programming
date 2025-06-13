#!/usr/bin/python3
"""Module that defines a Square class with size validation."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): length of a side (default is 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size  # routed through the setter for validation

    @property
    def size(self):
        """int: The length of the square’s side"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Validate and set the size of the square.

        Args:
            value (int): new side length

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
