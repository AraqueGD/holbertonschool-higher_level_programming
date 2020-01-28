#!/usr/bin/python3
""" Difine Base Class Module """

import json


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Building __init__ """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if (list_dictionaries is None):
            list_dictionaries = []
            return list_dictionaries
        else:
            return json.dumps(list_dictionaries)
