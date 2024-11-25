#!/usr/bin/python3
""" Module : 1. Divide a matrix """

def matrix_divided(matrix, div):
    # Vérification de la variable matrix
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        for listOfMatrix in matrix:
            if not isinstance(listOfMatrix, list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                for elementOfList in listOfMatrix:
                    if not isinstance(elementOfList, (int, float)):
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Vérification de la taille de chaque élement de la matrix
    sizeOfRow = len(matrix[0])
    for elementOfMatrix in range(1, len(matrix)):
        if len(matrix[elementOfMatrix]) != sizeOfRow:
            raise TypeError("Each row of the matrix must have the same size")
    # Vérification de la variable div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    # Effectuer la division de chaque élément de list
    # et retourner la nouvelle matrix
    newMatrix = []
    for listOfMatrix in matrix:
        newListOfMatrix = []
        for elementOfList in listOfMatrix:
            newElementOfList = "%.2f" % (elementOfList / div)
            newListOfMatrix.append(newElementOfList)
        newMatrix.append(newListOfMatrix)
    return newMatrix