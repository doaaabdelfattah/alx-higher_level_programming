#!/usr/bin/python3
def remove_char_at(str, n):
    strcopy = ''
    str_len = len(str)
    if n < 0 or n >= str_len:
        return str
    for idx in range(0, str_len):
        if idx != n:
            strcopy += str[idx]
    return strcopy
