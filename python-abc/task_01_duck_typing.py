#!/usr/bin/python3
"""Module defines abstract class"""


from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """Shape class"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Circle Class"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    """Rectangle Class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(arg1):
    print(f"Area: {arg1.area()}")
    print(f"Perimeter: {arg1.perimeter()}")

if __name__ == "__main__":
    c = Circle(5)
    r = Rectangle(4, 6)

    print("Circle (radius=5):")
    shape_info(c)

    print("\nRectangle (4x6):")
    shape_info(r)
