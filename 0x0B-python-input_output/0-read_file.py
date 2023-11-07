#!/usr/bin/python3
""" Reading File """

def read_file(filename=""):

    """ reads file contents and print it to stdout"""
    with open(filename, encoding="utf-8") as myfile:
        read_data = myfile.read()
        print(read_data)
