#!/usr/bin/python3
import os
""" writes to file"""

def write_file(filename="", text=""):
    """writes text to file"""
    with open(filename, "w", encoding="utf-8") as myfile:
        myfile.write(text)
    return len(text)
