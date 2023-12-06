#!/usr/bin/python3
""" write_file Function Module
"""


def append_write(filename="", text=""):
    '''  writes a string to a text file (UTF8)'''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
