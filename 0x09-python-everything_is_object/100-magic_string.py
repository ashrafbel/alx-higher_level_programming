#!/usr/bin/python3
def magic_string():
    magic_string.Ct = getattr(magic_string, 'Ct', 0) + 1
    return ', '.join(['BestSchool' for X in range(magic_string.Ct)])
