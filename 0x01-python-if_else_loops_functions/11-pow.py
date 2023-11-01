#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return -1
    else:
        pow = 0
        while pow < b:
            a = a * a
            pow += pow
    return a