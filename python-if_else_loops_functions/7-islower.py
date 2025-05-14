#!/usr/bin/python3

def islower(c):

    c = ord(c)

    for dec in range(97, 123):
        if c == dec:
            print(f"{chr(c)} is lower")
        else:
            print(f"{chr(c)} is upper")
