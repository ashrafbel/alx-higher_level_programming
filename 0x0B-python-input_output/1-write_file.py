#!/usr/bin/python3
"Def writefile fun"


def write_file(filename="", text=""):
    "read file using utf-8"
    U = "utf-8"
    with open(filename, "w", encoding=U) as f_l:
        W = (f_l.write(text))
        return W
