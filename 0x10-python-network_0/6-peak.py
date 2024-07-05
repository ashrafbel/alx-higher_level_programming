#!/usr/bin/python3
"defines a peak-finding algorithm"


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    r = len(list_of_integers) - 1
    lt = 0
    while lt < r:
        m = (lt + r) // 2

        if list_of_integers[m] > list_of_integers[m + 1]:
            r = m
        else:
            lt = m + 1
    return list_of_integers[lt]
