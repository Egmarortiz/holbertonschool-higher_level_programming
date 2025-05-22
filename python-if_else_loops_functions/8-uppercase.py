#!/usr/bin/python3

def to_upper(c):
    if 'a' <= c <= 'z':
        return chr(ord(c) - 32)
    return c

def uppercase(str):
    return ''.join(to_upper(c) for c in str)

print(uppercase("Jarvis is the best."))
