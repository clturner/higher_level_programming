#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) <= 0 or my_list == [] or my_list == None:
        return None
    new_list = list(my_list)
    new_list.reverse()
    for i in new_list:
        print('{:d}'.format(i))
