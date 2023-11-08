#!/usr/bin/python3
"""Defines a class"""

class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initialize object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
