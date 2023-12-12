#!/usr/bin/python3
''' Rectangle Module'''
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize new rectangle'''
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    # Getters
    @property
    def width(self):
        '''Set/get the width of the Rectangle.'''
        return self.__width

    @property
    def height(self):
        '''Set/get the height of the Rectangle.'''
        return self.__height

    @property
    def x(self):
        '''Set/get the x of the Rectangle.'''
        return self.__x

    @property
    def y(self):
        '''Set/get the y of the Rectangle.'''
        return self.__y

    # Setters
    @width.setter
    def width(self, value):
        '''Set/get the width of the Rectangle.'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''Set/get the height of the Rectangle.'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        '''Set/get the x of the Rectangle.'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        '''Set/get the y of the Rectangle.'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' area of Rectangle'''
        return self.width * self.height

    def display(self):
        ''' print # in stdout'''
        for row in range(self.height):
            print('#' * self.width)

    def __str__(self):
        '''string representation for class'''
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def display(self):
        ''' print Rectangle by character #'''
        [print("") for y in range(self.y)]
        for _ in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width, end='')
            print("")
        # for _ in range(self.height):
        #     for _ in range(self.x):
        #         print(" ", end='')
        #     for _ in range(self.width):
        #         print("#", end='')
        #     print("")

    def update(self, *args, **kwargs):
        ''' Update method'''
        if args and len(args) != 0:
            flag = 0
            for arg in args:
                if flag == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif flag == 1:
                    self.width = arg
                elif flag == 2:
                    self.height = arg
                elif flag == 3:
                    self.x = arg
                elif flag == 4:
                    self.y = arg
                flag += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    self.id = value
                if key == 'height':
                    self.height = value
                if key == 'width':
                    self.width = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        ''' Return Dict representation of Rectangle'''
        Rect_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
                }
        return Rect_dict
