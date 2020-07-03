#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if isinstance(first_name, str) and if last_name == None:
        return first_name
    print("My name is", first_name + " " + last_name)
