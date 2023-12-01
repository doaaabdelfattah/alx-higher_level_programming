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
    characters = ['.', '?', ':']
    result = ""
    skip_spaces = True
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for c in text:
        if skip_spaces and c == ' ':
            continue
        # Set the flag to False after
        # encountering the first non-space character
        skip_spaces = False

        result += c
        if c in characters:
            result += '\n'
    print(result)
