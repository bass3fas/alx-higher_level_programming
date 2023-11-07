#!/usr/bin/python3
"""Defines function saving json"""
import json


def save_to_json_file(my_obj, filename):
    """ writes json representation to file.
    Args:
    my_obj (list): object to represent
    filename (str): file which writing to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
