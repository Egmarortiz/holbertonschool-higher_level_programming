#!/usr/bin/python3

def islower(c):

    c = ord(c)

    if c < 97 or c > 122:
        print(f"{chr(c)} is upper")
    else:
        print(f"{chr(c)} is lower")
