from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape defined by its radius."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape defined by width and height."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def shape_info(shape: Shape) -> None:
    """
    Print the area and perimeter of any object
    that implements the Shape interface.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    c = Circle(5)
    r = Rectangle(4, 6)

    print("Circle (radius=5):")
    shape_info(c)

    print("\nRectangle (4x6):")
    shape_info(r)

