#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    for i in new_list:
        i = (i - 1)
        if idx >= len(my_list) or idx < 0:
            return my_list
        if i == idx:
            new_list.remove(my_list[i])
            new_list.insert(idx, element)
            return(new_list)
