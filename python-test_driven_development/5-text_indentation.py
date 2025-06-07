#!/usr/bin/python3

"""
Function text_indentation(text) prints text with two new lines
after each occurrence of '.', '?' or ':'.
"""


def text_indentation(text):

    """
    Prints a text with two new lines after '.', '?' and ':'.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
