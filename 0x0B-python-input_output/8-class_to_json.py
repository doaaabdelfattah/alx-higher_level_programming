#!/usr/bin/python3
""" Class to JSON Function Module
"""


def class_to_json(obj):
    '''  returns the dictionary description '''
    return obj.__dict__
