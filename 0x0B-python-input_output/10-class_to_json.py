#!/usr/bin/python
import json

def class_to_json(obj):
    return(json.loads(json.dumps(obj.__dict__)))
