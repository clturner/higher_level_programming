#!/usr/bin/pyhton3
"""
module with one function, add_integer(a,b )
"""

def add_integer(a, b):
    if isinstance(a, float) or isinstance(b, float):
        c = int(a) + int(b)
        return c
    if isinstance(a, int) and isinstance(b, int):
        return(a + b)
    else:
        if type(a) != int:
            raise TypeError("a must be an integer")
        elif type(b) != int:
            raise TypeError("b must be an integer")
        return (a + b)
