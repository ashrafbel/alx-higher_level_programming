#!/usr/bin/python3
def uppercase(in_str):
    for x in in_str:
        if ord(x) >= 97 and ord(x) <= 122:
            x = chr(ord(x) - 32)
        print("{}".format(x), end="")
    print("")
