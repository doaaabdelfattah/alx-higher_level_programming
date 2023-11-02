#!/usr/bin/python3
# Your code should not be executed when imported
if __name__ == "__main__":
    import hidden_4
# Make list of all names in module
name = dir(hidden_4)
for x in name:
    if name[x][:2] != '__':
        print("{}".format(name[x]))
