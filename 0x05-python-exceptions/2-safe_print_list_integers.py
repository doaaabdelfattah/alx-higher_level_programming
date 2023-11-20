#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        # ValueError (which could occur if a non-integer string is encountered)
        # TypeError to catch cases where the element in the list is not an integer. 
        except (ValueError, TypeError): 
            continue
        except IndexError:
            break
    print("")
    return (count)
