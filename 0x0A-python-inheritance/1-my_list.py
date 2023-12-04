#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    def print_sorted(self):
        """
        Print the sorted elements of the list.
        """
        print(sorted(self))
