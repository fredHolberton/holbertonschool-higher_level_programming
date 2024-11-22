#!/usr/bin/python3
""" Module : 0. Integers addition0. Integers addition """


def add_integer(a, b=98):
    """ Method wich add two integers and return the result """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
