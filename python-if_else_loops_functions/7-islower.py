#!/usr/bin/python3

def islower(c):
    """
    Returns True if character c is a lowercase letter (a–z), False otherwise.
    """

    if not isinstance(c, str) or len(c) != 1:
        return False

    return 'a' <= c <= 'z'
