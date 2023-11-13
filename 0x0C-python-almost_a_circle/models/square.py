#!/usr/bin/python3
"""Defining square inherited from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """intializing square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value


    def update(self, *args, **kwargs):
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.size = args[1]
            if num_args >= 3:
                self.x = args[2]
            if num_args >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    
    """string presentation"""
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
