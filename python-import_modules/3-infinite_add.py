#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    result = 0

    for num in args:
        result += int(num)

    print(result)
