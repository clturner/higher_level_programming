#!/usr/bin/python3
import json

class Student:
    """ Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.lastname = last_name
        self.age = age

    def to_json(self):
        return(json.loads(json.dumps(self.__dict__)))
