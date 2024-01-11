#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    DIRN = {K: V*2 for K, V in a_dictionary.items()}
    return DIRN
