#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for x in range(list_length)
        try:
           new_ele = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError: 
            print("out of range")
        finally:
            
            