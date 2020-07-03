#!/usr/bin/python3
def remove_char_at(str, n):
    c = -1
    string = ""
    for index in str:
        c = c + 1
        if n != c:
            string = string + str[c]
    return(string)
