#!/usr/bin/python3
''' Square Module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            flag = 0
            for arg in args:
                if flag == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif flag == 1:
                    self.size = arg
                elif flag == 2:
                    self.x = arg
                elif flag == 3:
                    self.y = arg
                flag += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def __str__(self):
        ''' String represetation of Square'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
