#!/usr/bin/python3
"""Implementing pickle module"""
import pickle

class CustomObject:
    """Implementing Pickle Module"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display Instance"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize Pickle"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except (FileNotFoundError, pickle.PickleError, Exception):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize Pickle"""
        try:
            with open(filename, 'rb') as f:
                loaded = pickle.load(f)
            return loaded
        except (FileNotFoundError, pickle.pickleError, Exception):
            return None
