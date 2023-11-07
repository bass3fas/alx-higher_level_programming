#!/usr/bin/python3
"""Defining Reading File function """


def read_file(filename=""):
    """ reads file contents and print it to stdout"""
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read, end="")
