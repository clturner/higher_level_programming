#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    score = 0
    for key, value in my_dict.items():
        if value > score:
            score = value
        if value == score:
            return key
