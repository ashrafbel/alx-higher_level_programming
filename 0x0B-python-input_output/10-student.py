#!/usr/bin/python3
"""Defi classStudent."""


class Student:
    "Describe a student."

    def __init__(self, first_name, last_name, age):
        "Create a new student instance."
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        "Obtain a dictionary for the Student representation."
        try:
            for a in attrs:
                if type(a) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        D = dict()
        for Ky, Vl in self.__dict__.items():
            if Ky in attrs:
                D[Ky] = Vl
        return D
