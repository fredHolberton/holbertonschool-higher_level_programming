#!/usr/bin/python3
"""module : 3. Area of a square"""


class Square:
    """This class allows to value a private property size"""
    def __init__(self, size=0):
        """Constructor method"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    
    def area(self):
        """Method area : calculate and return the area of the square"""
        return self.__size ** 2
