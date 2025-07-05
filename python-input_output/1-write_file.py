#!/usr/bin/python3
"""Writes text to a file"""

def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
        count = f.write(text)
    retuen count
