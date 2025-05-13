#!/usr/bin/python3

print("{}".format('\n'.join(f"{dec:d} = {dec:02x}" for dec in range(99))), end= '')
