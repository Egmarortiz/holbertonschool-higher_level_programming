#!/usr/bin/python3

print(
    "{}".format(
        ", ".join(
            f"{i}{j}"
            for i in range(9)
            for j in range(i + 1, 10)
        )
    ),
    end='\n'
)
