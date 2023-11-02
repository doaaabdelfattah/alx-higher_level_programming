#!/usr/bin/python3
# Your code should not be executed when imported
if __name__ == "__main__":
    import sys

allarg = len(sys.argv)
if allarg == 1:
    print("0 arguments.")
elif allarg == 2:
    print("{} argument:".format(allarg - 1))
else:
    print("{} arguments:".format(allarg - 1))

for x in range(1, allarg):
    print("{}: {}".format(x, sys.argv[x]))
