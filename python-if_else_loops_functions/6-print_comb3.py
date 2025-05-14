#!/usr/bin/python3

print(
    ", ".join(
        f"{i}{j}"
        for i in range(9)
        for j in range(i + 1, 10)
    )
)
