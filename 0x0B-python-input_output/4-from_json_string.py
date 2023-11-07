#!/usr/bin/python3
"""Defines function from json to python"""
import json


def from_json_string(my_str):
    """change from json representation to python"""
    return json.loads(my_str)
