#!/usr/bin/python3
"""Def fuction PascalTriangle """


def pascal_triangle(n):
    "Describe Pascal's Triangle with a size of n."
    if n <= 0:
        return []

    pas_tri = [[1]]
    while len(pas_tri) != n:
        T = pas_tri[-1]
        Tp = [1]
        for X in range(len(T) - 1):
            Tp.append(T[X] + T[X + 1])
        Tp.append(1)
        pas_tri.append(Tp)
    return pas_tri
