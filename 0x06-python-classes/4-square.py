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
        self.__size = size

    def size(self):
        """return current size (Getter)"""
        return self.__size

    def size(self, value):
        """Set the value (Setter)"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return current square area"""
        return (self.__size * self.__size)
