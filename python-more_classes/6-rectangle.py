#!/usr/bin/python3

#module 6

"""Module deines a rectangle"""


class Rectangle:
    """intilializes the counter"""
    number_of_instances = 0
    """Module defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        """adds an instance"""
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Module defines a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Module defines a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Module defines a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Module defines a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Module deines a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Module deines a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Module deines a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = []
        for _ in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)

    def __repr__(self):
        """Module defines a rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Module defines a rectangle"""
        """deletes an instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

