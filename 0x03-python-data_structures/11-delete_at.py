#!/usr/bin/python3
def delete_at(my_list=[], idx="0"):
    if idx < 0:
        return my_list
    new_list = []
    c = (len(my_list))
    if (c - 1) < idx:
        return my_list
    for i in my_list:
        new_list.append(i)
    new_list.remove(new_list[idx])
    my_list.remove(my_list[idx])
    return new_list
