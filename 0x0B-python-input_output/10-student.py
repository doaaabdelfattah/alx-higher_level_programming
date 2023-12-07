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
        if (type(attrs) is list):
            # if True create Dictionary using dictionary comprehension
            # 1) Iterate over each attribute name (K) in the list attrs
            # 2) For each attribute, it checks if the object (self) \
            # has that attribute using hasattr
            # 3) if exist: it add key-value pair to the dict where:
            #   a.Key is attribute
            #   b.Value is the value of attribute
            {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
