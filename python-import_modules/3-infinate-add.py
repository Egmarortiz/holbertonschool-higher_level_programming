#!/usr/bin/python3

import sys

args = sys.argv[1:]

result = 0

for num in args:
    result += num

print(result)
