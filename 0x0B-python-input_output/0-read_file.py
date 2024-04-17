#!/usr/bin/python3
"""Def function REad_file"""


def read_file(filename=""):
    """function read txt file"""
    U = "utf-8"
    with open(filename, encoding=U) as f_l:
        print(f_l.read(), end="")
