#!/usr/bin/python3

"""
Defines a function add_integer(a, b=98) that:
  - Raises a TypeError if a or b is not an int or float
  - Truncates floats toward zero (via int()) before adding
  - Returns the integer sum of int(a) + int(b)
"""

def add_integer(a, b=98):

    """
    Adds two numbers after validating they are int or float.
    Floats are truncated toward zero before addition.
    If either a or b is not an int/float, raises TypeError.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
