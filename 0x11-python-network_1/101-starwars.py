#!/usr/bin/python3
"""
sends a POST request to URL email as a parameter, displays response bod
"""
import requests
import sys


if __name__ == "__main__":

    r = requests.get('https://swapi.co/api/people/?search={}'.format(sys.argv[1]))
    data = r.json()
    print('Number of result: {}'.format(data['count']))
    for x in data.get('results'):
        print(x['name'])
