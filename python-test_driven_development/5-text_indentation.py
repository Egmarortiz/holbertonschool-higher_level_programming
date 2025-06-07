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

    buffer = ""
    length = len(text)
    i = 0

    while i < length:
        char = text[i]
        buffer += char
        if char in ".?:":
            print(buffer.strip(), end="\n\n")
            buffer = ""
            # skip spaces after punctuation
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1

    if buffer:
        print(buffer.strip())
