#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1.difference(set_2)
    other_new_set = set_2.difference(set_1)
    newest_set = new_set.union(other_new_set)
    return newest_set
