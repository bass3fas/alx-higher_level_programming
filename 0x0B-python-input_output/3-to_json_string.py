#!/usr/bin/python3
import json
""" Defines function prints json representation"""


def to_json_string(my_obj):
    """represent string in json
    Args:
    obj (list): object to represent
    Returns:
    json representation
    """
    return json.dumps(obj)
