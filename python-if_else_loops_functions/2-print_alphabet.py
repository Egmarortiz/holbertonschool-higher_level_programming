#!/usr/bin/python3

#list(map(chr, [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

#s = ['1', '2', '3', '4']
#res = map(int, s)
#print(list(res))

for abc in range(97, 123):
    if abc >= 65 or abc <= 91:
        print(f"{chr(abc)}")
