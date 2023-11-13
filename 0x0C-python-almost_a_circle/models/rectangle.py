#!/usr/bin/python3
"""Defines a clasee inherited from Base"""



class Rectangle(Base):
    """defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    """getter and setter for width"""
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value

    """getter and setter for height"""
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value

    """getter and setter for x"""
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value

    """getter and setter for y"""
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value
