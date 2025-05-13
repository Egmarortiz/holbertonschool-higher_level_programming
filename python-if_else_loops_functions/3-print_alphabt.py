#!/usr/bin/python3

for abc in range(97, 123):
    if abc == 113 or abc == 101:
        continue
    print(f"{chr(abc)}", sep= '', end = '')
