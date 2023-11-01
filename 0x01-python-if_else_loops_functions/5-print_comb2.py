#!/usr/bin/python3
for number in range(0, 100):
    if number < 99:
        print("{}, ".format(str(number).zfill(2)), end="")
    else:
        print("{}".format(str(number).zfill(2)),)
