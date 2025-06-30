#!/usr/bin/python3

"""Abstract animal class"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal class"""
    @abstractmethod
    def sound(self):
        """Abstract sound method"""
        pass

class Dog(Animal):
    """Dog Class"""
    def sound(self):
        """Inherited sound method"""
        print("Bark")

class Cat(Animal):
    """Cat class"""
    def sound(self):
        """Inherited sound method"""
        print("Meow")
