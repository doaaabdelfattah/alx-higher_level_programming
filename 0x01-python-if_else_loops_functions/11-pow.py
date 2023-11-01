#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        print('1')
        return 1
    elif b < 0:
        print('-1')
        return -1
    else:
        for b:
            a = a * a
    print("{}".format(a))
    return a