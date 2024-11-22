#!/usr/bin/python3
"""module : 4. Access and update private attribute"""


class Square:
    """This class allows to value a private property size"""
    def __init__(self, size=0):
        """Constructor method"""
        self.size = size

    def area(self):
        """Method area : calculate and return the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Method to get the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
