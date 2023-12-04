#!/usr/bin/python3
""" is_same_class Module """


def inherits_from(obj, a_class):
    """
    Return True if: Same class or inherit from
    """
    if issubclass(obj.__class__, a_class) and type(obj) is not a_class:
        return True
    return False
