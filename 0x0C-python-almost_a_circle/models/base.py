#!/usr/bin/python3
''' Base Module'''
import json


class Base:
    '''Class Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' return JSON string representation'''
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes JSON string representation to file'''
        lists_dicts = []
        # Create JSON file
        filename = cls.__name__ + ".json"
        # Create list of dictionaries
        for x in list_objs:
            lists_dicts.append(x.to_dictionary())
        # Format string to JSON format
        if list_objs is None:
            json_string = cls.to_json_string([])
        else:
            json_string = cls.to_json_string(lists_dicts)
        # Save to file
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''return list of JSON string'''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        dummy = cls(1, 1)

        dummy.update(**dictionary)
        return dummy
