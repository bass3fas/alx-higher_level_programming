#!/usr/bin/python3
"""Defines Function"""


def inherits_from(obj, a_class):
    """"check if inherited"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
