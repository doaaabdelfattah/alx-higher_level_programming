#!/usr/bin/python3
""" print_square Function Module
"""
def print_square(size):
    """
    print_square function that prints square with the character #.
    + Parameters:
        size: size length of the square
    + Raises:
        TypeError: If size isn't int.
        TypeError: If size < 0.
        TypeError: If size is a float and is less than 0, raise 

    + Prints:
        My name is <first name> <last name>
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    for _ in range(size):
            print('#' * size)