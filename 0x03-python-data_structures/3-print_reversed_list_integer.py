#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        n = 0
        my_list.reverse()
        while n < len(my_list):
            print("{:d}".format(my_list[n]))
            n += 1
