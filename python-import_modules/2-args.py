#!/usr/bin/python3


# File demo.py
import sys


def main():
    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    for index, arg in enumerate(args, start=1):
        print(f"{index}: {arg}")


if __name__ == "__main__":
    main()
