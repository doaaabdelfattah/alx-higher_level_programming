#!/usr/bin/python3
# Your code should not be executed when imported
if __name__ == "__main__":
    import hidden_4
# Make list of all names in module
namelist = dir(hidden_4)
for name in namelist:
    if name[:2] != '__':
        print("{}".format(name))
