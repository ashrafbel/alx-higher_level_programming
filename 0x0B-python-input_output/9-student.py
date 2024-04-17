#!/usr/bin/python3
"""Defi classStudent."""


class Student:
    "Describe a student."

    def __init__(self, first_name, last_name, age):
        "Create a new student instance."
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        "Obtain a dictionary for the Student representation."
        return self.__dict__
