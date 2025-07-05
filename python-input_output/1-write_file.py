#!/usr/bin/python3
"""Appends text to a file"""


def write_file(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(text)
    return count
