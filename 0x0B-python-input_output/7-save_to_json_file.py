#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w+') as data:
        a = json.dumps(my_obj)
        return(data.write(a))
