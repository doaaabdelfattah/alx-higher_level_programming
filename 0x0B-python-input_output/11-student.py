#!/usr/bin/python3
''' Student class '''


class Student:
    ''' studen class definition'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation'''
        if (type(attrs) is list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        ''' replaces all attributes of the Student instance:'''
        for key, value in json:
            if hasattr(self, key):
                setattr(self, key, value)
