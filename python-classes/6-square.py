#!/usr/bin/python3
"""Module 3-square: defines a Square."""


class Square:
    """Module 3-square: defines a Square."""
    def __init__(self, size=0, position(0, 0)):
        """Module 3-square: defines a Square."""
        self.__size = size
        self._position = position

    @property
    def size(self):
        """Module 3-square: defines a Square."""
        return self.__size

    @size.getter
    def size(self, value):
        """Module 3-square: defines a Square."""
        if not isinstance(size, int):
            raise TypeError("size must be an int")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Module 3-square: defines a Square."""
        return self.__position

    @position.getter
    def position(self, value):
        """Module 3-square: defines a Square."""
        if (
            not isinstance(position, tuple)
            or len(position) != 2
            or not all (isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be  a tuple of 2 positive integers")
        self.__positioon = value

    def area(self):
        """Module 3-square: defines a Square."""
        return self.__size ** 2

    def my_print(self):
        """Module 3-square: defines a Square."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print("#" * self.__size)
