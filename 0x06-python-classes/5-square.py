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

    @property
    def size(self):
        """Get/Set the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
