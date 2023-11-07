#!/usr/bin/python3
import os
""" writes to file"""

def append_write(filename="", text=""):
    """appends text to file"""
    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)
