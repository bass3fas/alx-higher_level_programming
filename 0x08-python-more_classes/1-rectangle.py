#!/usr/bin/python3
""" Class Defines a rectangle"""


class Rectangle:
    """ represents a rectangle """
    def __init__(self, width=0, height=0):
        """ Initialize rectangle.
        Args:
        width(int) : width of rectangle
        height(int) : height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get rectangle width """
        return self.__width

    @property.setter
    def width(self, value):
        if not ininstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get rectangle height """
        return self.__height

    @property.setter
    def height(self, value):
        if not ininstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
