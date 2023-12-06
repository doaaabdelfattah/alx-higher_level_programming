#!/usr/bin/python3
''' Student class '''


class Student:
    ''' studen class definition'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if type(attrs) is list:
            return (self.first_name, self.last_name)
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json:
            if hasattr(self, key):
                setattr(self, key, value)
