#!/usr/bin/python3
""" Module : 3. Print square """


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    else:
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                if j < size:
                    print("#", end='')
                else:
                    print("#", end='\n')
