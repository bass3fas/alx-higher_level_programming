#!/usr/bin/python3
"""Defines function writes to file"""


def write_file(filename="", text=""):
    """writes text to file

    Args:
    filename (str): file to write to
    text (str): text to write
    Returns:
    number of chr written
    """
    with open(filename, "w", encoding="utf-8") as myfile:
        return myfile.write(text)
