#!/usr/bin/python3

print("{}".format('\n'.join(f"{dec:d} = {hex(dec)}" for dec in range(99))),
      end='\n')
