#!/usr/bin/python3
""" is_same_class Module """


def is_same_class(obj, a_class):
    """
    returns True if the object is an instance of the specified class
    """
    if type(obj) is a_class:
        return True

    return False
