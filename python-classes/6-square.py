#!/usr/bin/python3
"""module : 6. Coordinates of a square"""


class Square:
    """This class allows to value a private property size"""
    def __init__(self, size=0, position(0, 0)):
        """Constructor method"""
        self.size = size
        self.position = position

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
                for s in range(1, self.position[0] + 1):
                    print(" ", end='')
                for j in range(1, self.size + 1):
                    if j < self.size:
                        print("#", end='')
                    else:
                        print("#", end='\n')

    @property
    def position(self):
        """Method to get position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """Method to set position value"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(value[0], int) and isinstance(value[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
