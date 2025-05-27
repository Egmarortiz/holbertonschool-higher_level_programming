#!/usr/bin/python3

def no_c(my_string):

    number = [ord(x) for x in my_string
              if my_string == 43 or my_string == 63
              continue]

    reverse = ''.join(chr(x) for x in number)

    return reverse
