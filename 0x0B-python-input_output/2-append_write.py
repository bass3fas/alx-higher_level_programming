#!/usr/bin/python3
"""Defines function appends to file"""


def append_write(filename="", text=""):
    """writes text to file

    Args:
    filename (str): file to write to
    text (str): text to write
    Returns:
    number of chr written
    """
    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)
