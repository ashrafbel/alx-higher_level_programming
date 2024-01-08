#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    RESULT = []
    for X in my_list:
        RESULT.append(True if X % 2 == 0 else False)
    return RESULT
