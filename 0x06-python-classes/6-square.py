#!/usr/bin/python3
"""Module Definition"""


class Square:
    """This is Class Square definition
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square object

        Args:
            size: square size(pivate)
            position: tuble of two.
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """Retrieve position """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
