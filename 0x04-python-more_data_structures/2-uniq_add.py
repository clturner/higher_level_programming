#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    my_set = set(my_list)
    for j in my_set:
        count = count + j
    return count
