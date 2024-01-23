#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    valueisinteger = True
    try:
        print("{:d}".format(value))
        return valueisinteger
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        valueisinteger = False
        return valueisinteger
