#!/usr/bin/python3
"""Defining id for all other classes"""
import json


class Base():
    """Defines a Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        if list_objs is None:
            return []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:

            new_list = []
            for i in list_objs:
                dictionary = i.to_dictionary()
                new_list.append(dictionary)
            return f.write(Base.to_json_string(new_list))

    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
