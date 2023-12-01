#!/usr/bin/python3
""" add_integer Function Module
"""


def add_integer(a, b=98):
    """
    add_interger function that add two numbers

    Parameters:
    a (int): number 1.
    b (int): number 2.

    Returns:
    int: addition of two values.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
