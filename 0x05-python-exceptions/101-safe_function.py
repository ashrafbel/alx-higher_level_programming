#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        re_val = fct(*args)
        return re_val
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        return None
