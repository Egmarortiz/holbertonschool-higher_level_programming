#!/usr/bin/python3

def islower(c):

    #  code = ord(c)

   # if code < 97 or code > 122:
    #    print(f"{chr(code)} is upper")
   # else:
    #    print(f"{chr(code)} is lower")

    if not isinstance(c, str) or len(c) != 1:
        return False

    return c.islower()

if __name__ == "__main__":
    tests = ['a', 'Z', 'm', '1', '', 'ab']
    for ch in tests:
        print(f"{repr(ch)} -> {islower(ch)}")
