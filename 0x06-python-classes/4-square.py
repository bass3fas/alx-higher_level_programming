#!/usr/bin/python3
""" Defining square"""
class Square:
    """ defining init """
    def __init__(self, size = 0):
        """ intialize a new square.
        Args:
            size(int): size of new square
        """
        self.size = size
    @property
    def size(self):
        """ set the size of a square"""
        return (self.size)

    @setter
    def size(self, value):
        if not isisntance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.size = value
    def area(self):
        """ setting area of square"""
        return (self.size * self.size)
