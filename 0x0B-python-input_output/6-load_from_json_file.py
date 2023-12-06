#!/usr/bin/python3
""" write_file Function Module
"""
import json


def load_from_json_file(filename):
    ''' writes an Object to a text file, using a JSON representation'''
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))
