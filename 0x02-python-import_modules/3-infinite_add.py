#!/usr/bin/python3
# Your code should not be executed when imported
if __name__ == "__main__":
    import sys

allarg = len(sys.argv)
result = 0
for x in range(1, allarg):
    result += int(sys.argv[x])
print(result)
