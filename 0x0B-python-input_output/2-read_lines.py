#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    count = 0
    with open(filename, 'r') as data:
        if nb_lines <= 0:
            for line in data:
                print(line, end="")
        for line in data:
            if count is not nb_lines:
                print(line, end="")
                count += 1
