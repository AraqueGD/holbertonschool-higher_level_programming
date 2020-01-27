#!/usr/python3

from models.base import Base
""" Difine Rectangle Class Module """


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for Width """
        return(self.__width)

    @property
    def height(self):
        """ Getter for heigth """
        return(self.__height)

    @property
    def x(self):
        """ Getter for x """
        return(self.__x)

    @property
    def y(self):
        """ Getter for y """
        return(self.__y)

    @width.setter
    def width(self, value):
        """ Setter for width """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Setter for height """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ Setter for x """
        if (type(value) != int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ Setter for y """
        if (type(value) != int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Function area the Rectangle """
        return (self.__width * self.height)

    def display(self):
        """ Display # Rectangle """
        for nline in range(self.y):
            print('')
        for h in range(self.height):
            print(' ' * self.x, end='')
            for w in range(self.width):
                print('#', end='')
            print('')

    def __str__(self):
        """ Return __str__ method """
        return ("[{self.__class__.__name__}] ({}) {}/{} - {}/{}"
                .format(self.id,
                        self.__x,
                        self.__y,
                        self.__width,
                        self.__height,
                        self=self))

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            idx = 0
            for arg in args:
                if idx == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif idx == 1:
                    self.width = arg
                elif idx == 2:
                    self.height = arg
                elif idx == 3:
                    self.x = arg
                elif idx == 4:
                    self.y = arg
                idx += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if (key == 'id'):
                    if (value == None):
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif (key == 'width'):
                    self.width = value
                elif (key == 'height'):
                    self.height = value
                elif (key == 'x'):
                    self.x = value
                elif (key == 'y'):
                    self.y = value
