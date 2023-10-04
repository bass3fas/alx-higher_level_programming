#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            upper = chr(ord(char) - 32)
            print("{}".format(upper), end='')
        else:
            print("{}".format(char), end='')
    print()
