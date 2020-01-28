#!/usr/python3
from models.rectangle import Rectangle
""" Difine Square Class Module """


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size """
        return (self.width)

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Return __str__ method """
        return ("[{self.__class__.__name__}] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width, self=self))

    def update(self, *args, **kwargs):
        """ Update Attributes with Args"""
        if (args and len(args) != 0):
            idx = 0
            for arg in args:
                if (idx == 0):
                    if (arg == None):
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif (idx == 1):
                    self.size = arg
                elif (idx == 2):
                    self.x = arg
                elif (idx == 3):
                    self.y = arg
                idx += 1
        elif (kwargs and len(kwargs) != 0):
            for key, value in kwargs.items():
                if (key == 'id'):
                    if (value == None):
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif (key == 'size'):
                    self.size = value
                elif (key == 'x'):
                    self.x = value
                elif (key == 'y'):
                    self.y = value

    def to_dictionary(self):
        """ Return the dictionary representation of the Square """
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y,
                }
