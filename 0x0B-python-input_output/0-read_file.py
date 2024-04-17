#!/usr/bin/python3
"""Def function REad_file"""


def read_file(filename=""):
    """function read txt file"""
    with open(filename, encoding="utf-8") as f_l:
        print(f_l.read(), end="")
