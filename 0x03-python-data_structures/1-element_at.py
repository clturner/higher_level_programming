#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx > len(my_list) - 1 or idx < 0):
        return None
    else:
        for i in my_list:
            i = (i - 1)
            if i == idx:
                return my_list[i]
