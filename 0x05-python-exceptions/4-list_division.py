#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        try:
            new_ele = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            new_ele = 0
        except TypeError:
            print("wrong type")
            new_ele = 0
        except IndexError:
            print("out of range")
            new_ele = 0
        finally:
            new_list.append(new_ele)
    return new_list
