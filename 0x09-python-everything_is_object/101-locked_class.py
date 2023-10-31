#!/usr/bin/python3
"""Define a class locked"""



class LockedClass:
    """ prevents user from creating any
    new attribute except for first_name
    """
    __slots__ = ("first_name",)
