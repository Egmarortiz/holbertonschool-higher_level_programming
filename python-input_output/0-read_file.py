#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
