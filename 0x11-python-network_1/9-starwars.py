#!/usr/bin/python3
"""
sends a POST request to URL email as a parameter, displays response bod
"""
import requests
import sys

if __name__ == "__main__":

    r = requests.get('https://swapi.co/api/people/?search={}'.format(sys.argv[1]))
    r = r.json()
    print('Number of result: {}'.format(r['count']))
    for x in r.get('results'):
        print(x['name'])
