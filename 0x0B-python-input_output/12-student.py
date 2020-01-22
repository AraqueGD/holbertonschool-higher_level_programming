#!/usr/bin/python3
class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new = {}
        if (type(attrs) is list):
            for i in attrs:
                if i in self.__dict__:
                    new[i] = self.__dict__[i]
            return new
        return self.__dict__
