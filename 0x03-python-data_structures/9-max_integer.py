#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    MAX = my_list[0]
    for N in my_list:
        if N > MAX:
            MAX = N
    return MAX
