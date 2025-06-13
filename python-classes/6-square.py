#!/usr/bin/python3
"""Module 5-square: defines a Square."""


class Square:
    """Represents a square defined by its side length and print position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: length of the square’s side."""
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

    @property
    def position(self):
        """tuple: horizontal and vertical offsets for printing the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Validate and set the print position.

        Args:
            value (tuple): must be a tuple of 2 positive integers

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the current square area.

        Returns:
            int: area computed as size * size
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character, respecting position.

        - Prints `position[1]` blank lines before the square.
        - Each square line is prefixed by `position[0]` spaces.
        - If size is 0, prints a single blank line.
        """
        if self.__size == 0:
            print()
            return

        # vertical offset
        for _ in range(self.__position[1]):
            print()

        # square rows
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
