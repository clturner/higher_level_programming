#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupA = list(tuple_a)
    tupA.append(0)
    tupA.append(0)
    tupB = list(tuple_b)
    tupB.append(0)
    tupB.append(0)
    sum1 = tupA[0] + tupB[0]
    sum2 = tupA[1] + tupB[1]
    new_tuple = (sum1, sum2)
    return new_tuple
