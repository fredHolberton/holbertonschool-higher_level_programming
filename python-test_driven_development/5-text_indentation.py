#!/usr/bin/python3
""" Module : 4. text indentation """


def text_indentation(text):
    """ Method that print a new line after a ., ? or : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in [".", "?", ":"]:
            print("\n")
        if i + 1 < len(text) and text[i + 1] == " ":
            i += 1
        i += 1
