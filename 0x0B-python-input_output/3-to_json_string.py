#!/usr/bin/python3
""" Defines function prints json representation"""
import json


def to_json_string(my_obj):
    """represent string in json
    Args:
    my_obj (list): object to represent
    Returns:
    json representation
    """
    return json.dumps(my_obj)
