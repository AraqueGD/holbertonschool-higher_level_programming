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
    def width(self, width):
        """ Setter for width """
        self.__width = width

    @height.setter
    def height(self, height):
        """ Setter for height """
        self.__height = height

    @x.setter
    def x(self, x):
        """ Setter for x """
        self.__x = x

    @y.setter
    def y(self, y):
        """ Setter for y """
        self.__y = y
