#!/usr/bin/python3
""" Rectangle class
"""


class Rectangle:
    """
    This is Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
            Initialize rectangle class
        args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """ area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    @property
    def width(self):
        """ get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            return (
                '\n'.join(['#' * self.__width for _ in range(self.__height)])
                )

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
