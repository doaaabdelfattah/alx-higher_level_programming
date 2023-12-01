#!/usr/bin/python3
""" text_indentation Function Module
"""


def text_indentation(text):
    """
    text_indentation function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    + Parameters:
        text: must be string.
    + Raises:
        TypeError: If text is nor string
    """
    characters = [',', '?', ':']
    result = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in text:
        result += c
        if c in characters:
            result += '\n'
    print(result)
