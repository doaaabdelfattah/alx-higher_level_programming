#!/usr/bin/python3
idx = 0
for letter in reversed(range(ord('a'), ord('z') + 1)):
    print("{}".format(chr(letter - idx)), end="")
    if letter % 2 == 0:
        idx = 32
    else:
        idx = 0
