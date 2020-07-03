#!/usr/bin/python3


def write_file(filename="", text=""):
    with open(filename, 'w') as data:
        return data.write(text)
