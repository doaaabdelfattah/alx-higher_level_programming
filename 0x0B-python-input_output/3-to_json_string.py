#!/usr/bin/python3
""" write_file Function Module
"""
import json

def to_json_string(my_obj):
    '''  writes a string to a text file (UTF8)'''
    return json.dumps(my_obj)
