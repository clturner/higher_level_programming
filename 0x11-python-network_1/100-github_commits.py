#!/usr/bin/python3
"""
sends a POST request to URL email as a parameter, displays response bod
"""
import requests
import sys


if __name__ == "__main__":

    count = 0
    a = sys.argv[2]
    b = sys.argv[1]
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(a, b))
    commit_data = r.json()
    for x in commit_data:
        if count < 10:
            print(x['sha'], end="")
            print(": ", end="")
            print(x['commit']['author']['name'])
            count = count + 1
