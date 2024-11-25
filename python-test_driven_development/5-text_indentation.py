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
            j = i + 1
            while j < len(text) and text[j] == " ":
                j += 1
            i = j - 1
        i += 1
