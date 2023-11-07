#!/usr/bin/python3
"""Defines function saving json"""
import json


def load_from_json_file(filename):
    """ load json representation to file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
