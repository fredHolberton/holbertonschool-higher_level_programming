#!/usr/bin/python3
def uppercase(str):
    returnedStr = ''
    for c in str:
        if ord(c) >= ord("a") and ord(c) <= ord("z"):
            returnedStr = returnedStr + chr(ord(c) - 32)
        else:
            returnedStr = returnedStr + c
    print("{}".format(returnedStr), end='\n') 
