#!/usr/bin/python3
"Module defining the base class"
from json import dumps, loads
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        "writes the JSON string representation of list_objs"
        if list_objs is not None:
            list_objs = [ob.to_dictionary() for ob in list_objs]
        J = f"{cls.__name__}.json"
        U = "utf-8"
        with open(J, "w", encoding=U) as fl:
            fl.write(cls.to_json_string(list_objs))

    @classmethod
    def from_json_string(json_string):
        "returns the list as a json_string representation"
        if json_string is None or not json_string:
            x = []
            return x
        else:
            L = loads(json_string)
            return L

    @classmethod
    def create(cls, **dictionary):
        "create and returns an instance with attr"
        if cls.__name__ == "Rectangle":
            Newinstance = cls(1, 1)
        elif cls.__name__ == "Square":
            Newinstance = cls(1)
        Newinstance.update(**dictionary)
        return Newinstance

    @classmethod
    def load_from_file(cls):
        "Load instances from a file."
        fl_name = "{}.json".format(cls.__name__)
        if not os.path.exists(fl_name):
            return []
        with open(fl_name, "r", encoding="utf-8") as fl:
            data_json = fl.read()
            dict_s = cls.from_json_string(data_json)
            instances = [cls.create(**data) for data in dict_s]
            return instances
