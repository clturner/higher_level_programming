#!/usr/bin/python3
"""
sends a POST request to URL email as a parameter, displays response bod
"""
import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) == 1:
        payload = ""
    else:
        payload = sys.argv[1]
    parameter = {'q': payload}
    r = requests.post('http://0.0.0.0:5000/search_user', parameter)
    try:
        data = r.json()
    except ValueError as e:
        print("Not a valid JSON")
    if data:
        print('[{}] {}'.format(data['id'], data['name']))
    else:
        print("No result")
