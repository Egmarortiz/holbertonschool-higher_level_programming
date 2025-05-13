#!/usr/bin/python3

print("{}".format(', '.join(f"{num:02}" for num in range(100))),
      end='\n')
