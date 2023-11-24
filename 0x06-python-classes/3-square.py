#!/usr/bin/python3
"""Module Definition"""


class Square:
    """This is Class Square definition
    """

    def __init__(self, size=0):
        """Initialize Square object

        Args:
            size: square size(pivate)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return current square area"""
        return (self.__size * self.__size)
