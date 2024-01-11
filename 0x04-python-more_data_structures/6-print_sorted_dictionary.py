#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    L = sorted(a_dictionary.keys())
    for key in L:
        print("{}: {}".format(key, a_dictionary[key]))
