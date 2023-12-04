#!/usr/bin/python3
''' Geometry module '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


# The class Rectangle is a subclass of BaseGeometry.
class Rectangle(BaseGeometry):
    ''' BaseGeometry Class '''
    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
