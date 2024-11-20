#!/usr/bin/python3
def uppercase(str):
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
       print("{}".format(chr(ord(c) - 32)), end='')
    else:
       print("{}".format(c), end='') 
