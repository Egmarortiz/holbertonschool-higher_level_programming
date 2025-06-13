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
        return self.__size ** 2#!/usr/bin/python3
"""Module 3-square: defines a Square class with size validation and area calculation."""

class Square:
    """Represents a square with validated size and an area method."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): length of a side (default is 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size  # route through setter for validation

    @property
    def size(self):
        """int: the length of the square’s side."""
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

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            int: area computed as size * size
        """
        return self.__size ** 2
