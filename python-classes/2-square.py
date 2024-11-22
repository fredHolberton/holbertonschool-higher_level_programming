#!/usr/bin/python3
"""module : 2. Size validation"""


class Square:
    """This class allows to value a private property size"""
    def __init__(self, size=0):
        """Constructor method"""
        if isinstance(size, int) == False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
