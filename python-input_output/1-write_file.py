#!/usr/bin/python3
"""Writes text to a file"""

def write_file(filename="", text=""):
    """Writes text in a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        count = f.write(text)
    return count
