#!/usr/bin/python3

 """
    Prints a square using the '#' character.

    Args:
        size (int): the size length of the square.

    Raises:
        TypeError: size must be an integer.
        ValueError: size must be >= 0.
    """


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for sqr in range(size):
        print("#" * size)
