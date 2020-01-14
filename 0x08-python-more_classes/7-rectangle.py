#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        string = ""
        if (self.width is 0 or self.__height is 0):
            return ""
        for i in range(self.__height):
            for x in range(self.__width):
                try:
                    string += str(self.print_symbol)
                except Exception:
                    string += type(self).print_symbol
            if (i != self.height - 1):
                string = string + "\n"
        return string

    def __repr__(self):
        return ('{self.__class__.__name__}({}, {})'.
                format(self.__width, self.__height, self=self))

    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.width * self.__height)

    def perimeter(self):
        if (self.width is 0 or self.__height is 0):
            return 0
        else:
            return (2 * (self.width + self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
