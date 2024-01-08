#!/usr/bin/python3
def no_c(my_string):
    NSTR = ""
    for X in my_string:
        if X not in ("c", "C"):
            NSTR += X
    return NSTR
