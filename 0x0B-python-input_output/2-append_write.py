#!/usr/bin/python3
"""Def funtion AppendFile"""


def append_write(filename="", text=""):
    "append str using utf-8"
    U = "utf-8"
    with open(filename, "a", encoding=U) as f_l:
        A = f_l.write(text)
        return A
