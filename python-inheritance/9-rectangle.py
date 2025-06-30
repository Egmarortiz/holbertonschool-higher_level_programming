#!/usr/bin/python3
"""Module defines a rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """Initaialize and validate parameters"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        print(f"[Rectangle] {self.__width}/{self.__height}")
