#!/usr/bin/python3
"""module : 5. Printing a square"""


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

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(1, self.size + 1): 
                for j in range(1, self.size + 1):
                    if j < self.size:
                        print("#", end = '')
                    else:
                        print("#", end = '\n')
