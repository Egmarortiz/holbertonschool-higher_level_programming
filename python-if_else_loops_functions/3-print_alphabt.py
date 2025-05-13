#!/usr/bin/python3


print("{}".format(''.join(
    chr(i) for i in range(97, 123)
    if i not in (ord('e'), ord('q'))
)), end='')
