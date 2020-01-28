#!/usr/bin/python3
""" Difine Base Class Module """

import json
import os
import csv


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
        """ Json String function """
        if (list_dictionaries is None):
            list_dictionaries = []
            return list_dictionaries
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save to fule json """
        json_file = cls.__name__ + '.json'
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(json_file, 'w') as fle:
            fle.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ From json to string """
        if (json_string is None):
            string = []
            return string
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create a instance """
        if (cls.__name__ is "Rectangle"):
            instance = cls(1, 1)
        elif (cls.__name__ is "Square"):
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ Load from file json """
        file_json = cls.__name__ + ".json"
        new_list = []
        if os.path.isfile(file_json):
            with open(file_json, 'r') as f:
                new_list = cls.from_json_string(f.read())
            for i, j in enumerate(new_list):
                new_list[i] = cls.create(**new_list[i])
            return new_list
        else:
            return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save to file csv """
        file_cvs = cls.__name__ + ".csv"
        with open(file_cvs, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load file csv Function """
        file_json = cls.__name__ + ".csv"
        try:
            with open(file_json, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
