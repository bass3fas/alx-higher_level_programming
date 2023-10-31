#!/usr/bin/python3

"""
This is the "example" module.

The example module supplies one function, add_integer().  For example,

>>> add_integer(2, 3)
5
"""
def add_integer(a, b=98):
    """ Returns an Integer, the addition of a and b.
    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise ValueError("b must be an integer")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    return (a + b)
