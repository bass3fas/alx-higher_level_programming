#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            upper = chr(ord(char) - 32)
            print(upper, end='')
        else:
            print(char, end='')
    print()
