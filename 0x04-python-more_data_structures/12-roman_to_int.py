#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    rslt = 0
    preval = 0
    for X in reversed(roman_string):
        preval = roman_dict[X]
        rslt += preval if rslt < preval * 5 else -preval
    return rslt
