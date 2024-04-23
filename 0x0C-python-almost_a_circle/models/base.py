#!/usr/bin/python3
"Module defining the base class"
from json import dumps, loads


class Base:
    "Base class responsible for handling unique identifiers."
    __nb_objects = 0

    def __init__(self, id=None):
        "Initializes an instance"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        "return json str representaton list dict"
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            D = dumps(list_dictionaries)
            return D
