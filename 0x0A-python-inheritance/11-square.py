#!/usr/bin/python3
''' Square module '''
Rectangle = __import__('9-rectangle').Rectangle


# The class Square is a subclass of the class Rectangle.
class Square(Rectangle):
    ''' Square class '''
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__width}/{self.__height}"
