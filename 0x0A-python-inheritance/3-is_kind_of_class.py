#!/usr/bin/python3
""" Defines Function"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or inherits from, the specified class."""
    return isinstance(obj, a_class)
