#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resultofdive = a / b
    except ZeroDivisionError:
        resultofdive = None
    finally:
        print("Inside result: {}".format(resultofdive))
        return resultofdive
